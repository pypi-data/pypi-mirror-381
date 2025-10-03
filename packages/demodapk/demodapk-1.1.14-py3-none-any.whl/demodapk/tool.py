"""
APK tool utilities module.

This module provides functionality for:
- Downloading files with progress tracking
- Managing APKEditor downloads
- Handling GitHub releases
- Progress bar visualization

Based on: https://github.com/textualize/rich/blob/master/examples/downloader.py
"""

import json
import os
import signal
import sys
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from threading import Event
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from rich.align import Align
from rich.panel import Panel
from rich.progress import Progress  # TextColumn,
from rich.progress import (
    BarColumn,
    DownloadColumn,
    TaskID,
    TimeRemainingColumn,
    TransferSpeedColumn,
)

from demodapk.utils import console

# === Rich progress setup ===
progress = Progress(
    DownloadColumn(),
    "•",
    BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    TransferSpeedColumn(),
    "•",
    TimeRemainingColumn(),
    console=console,
)

done_event = Event()


def handle_sigint(*_):
    """Handle SIGINT (Ctrl+C) signal to stop downloads gracefully."""
    done_event.set()


signal.signal(signal.SIGINT, handle_sigint)


# === File download function ===
def copy_url(task_id: TaskID, url: str, path: str) -> None:
    """
    Copy data from a URL to a local file with progress tracking.

    Args:
        task_id (TaskID): Progress bar task identifier
        url (str): Source URL to download from
        path (str): Destination file path

    Returns:
        None

    Raises:
        URLError: If URL cannot be accessed
        HTTPError: If HTTP request fails
        OSError: If file cannot be written
    """
    progress.console.log(f"Requesting: {url}")
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req) as response:
        # Break if content length is missing
        total = response.info().get("Content-Length")
        total = int(total) if total is not None else 0

        progress.update(task_id, total=total)
        with open(path, "wb") as dest_file:
            progress.start_task(task_id)
            for data in iter(partial(response.read, 32768), b""):
                dest_file.write(data)
                progress.update(task_id, advance=len(data))
                if done_event.is_set():
                    return
    progress.console.log(f"Downloaded: '{os.path.basename(path)}'")


def download(urls: list[str], dest_dir: str = ".") -> None:
    """
    Download multiple files to the specified directory.

    Downloads files in parallel using a thread pool and displays
    progress for each download.

    Args:
        urls (list[str]): List of URLs to download
        dest_dir (str, optional): Destination directory. Defaults to current directory.

    Returns:
        None

    Raises:
        OSError: If destination directory cannot be created
    """
    os.makedirs(dest_dir, exist_ok=True)
    with progress:
        with ThreadPoolExecutor(max_workers=4) as pool:
            for url in urls:
                filename = url.split("/")[-1]
                dest_path = os.path.join(dest_dir, filename)
                task_id = progress.add_task("download", filename=filename, start=False)
                pool.submit(copy_url, task_id, url, dest_path)


def get_latest_version() -> str | None:
    """
    Get the latest version of APKEditor from GitHub API.

    Queries the GitHub releases API to get the most recent version tag.
    Handles version strings with or without leading 'V'/'v' prefix.

    Returns:
        str | None: Version string without prefix, or None if version cannot be determined

    Raises:
        SystemExit: If GitHub API request fails
    """
    url = "https://api.github.com/repos/reandroid/apkeditor/releases/latest"
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req) as resp:
            data = json.load(resp)
            tag_name = data.get("tag_name")
            if tag_name:
                # Remove leading 'V' if present
                return tag_name.lstrip("Vv")
    except (URLError, HTTPError) as e:
        progress.console.log(e)
        sys.exit(1)
    return None


def download_apkeditor(dest_path: str) -> None:
    """
    Download the latest version of APKEditor.

    Gets the latest version number and downloads the corresponding JAR file.
    Shows download progress using rich progress bars.

    Args:
        dest_path (str): Directory to save the APKEditor JAR

    Returns:
        None

    Raises:
        SystemExit: If version cannot be determined or download fails
    """
    latest_version = get_latest_version()
    if latest_version:
        progress.console.print(
            Panel(Align.center(f"APKEditor V{latest_version}"), expand=True),
            style="bold cyan",
        )
        jar_url = (
            "https://github.com/REAndroid/APKEditor/releases/download/"
            f"V{latest_version}/APKEditor-{latest_version}.jar"
        )
        download([jar_url], dest_path)
    else:
        progress.console.log("Could not determine the latest version.")
