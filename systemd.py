#! /usr/bin/env python3
import getpass
import os
from pathlib import Path
from rich import print

from obsidian_sync.config import settings


def generate_service_file():
    # Get the current user and home directory
    user = getpass.getuser()
    
    home_dir = str(Path.home())

    # Define the project directory and script name
    script_name = "obsidian_sync"

    # Path to the Poetry environment file
    env_python = str(settings.ROOT_PATH / "venv" / "bin" / "python")

    # Content of the systemd service file
    service_content = (
        "[Unit]\n"
        "Description=Obsidian Sync Service by Nehz (https://arturboyun.t.me)\n"
        "After=network.target\n\n"
        "[Service]\n"
        f"User={user}\n"
        f"WorkingDirectory={settings.ROOT_PATH}\n"
        f"ExecStart=/usr/bin/env bash -c '{env_python} -m {script_name}'\n"
        "Restart=always\n\n"
        "[Install]\n"
        "WantedBy=multi-user.target\n"
    )

    # Create the systemd service file

    try:
        # Writing to the systemd service file
        settings.SYSTEMD_SERVICE_SAVE_PATH.write_text(service_content.strip())

        print(
            f"[green bold]Service file created at [blue]{settings.SYSTEMD_SERVICE_SAVE_PATH}"
        )

    except PermissionError as e:
        print(
            f"[red bold]Permission denied: [blue]Unable to write to {settings.SYSTEMD_SERVICE_PATH}. Try running the script as root or using sudo."
        )
        print(e)


if __name__ == "__main__":
    generate_service_file()
