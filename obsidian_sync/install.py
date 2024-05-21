import os
from pathlib import Path
import time

from rich.progress import Progress
from obsidian_sync.config import settings
from rich import print

from obsidian_sync.user_settings import UserSettings, UserSettingsManager
from systemd import generate_service_file


class Installer:
    obsidian_vault_path: str | Path | None = None
    github_repo_url: str | None = None

    def __init__(self, user_settings_manager: UserSettingsManager):
        self.user_settings_manager = user_settings_manager

    def start(self):
        Installer.welcome_banner()

        if self.update_current_settings():
            print("Welcome to the Obsidian Sync installer!")
            print("Please answer the following questions to get started.\n")

            self.start_interactive_shell()

        print("[green bold]Updating the Obsidian Sync service...")
        generate_service_file()
        print("[green bold]Systemd service updated successfuly!")

        print(
            "\n\n[red bold]!!! Now you need to run the following commands to start the service !!!"
        )
        print(
            f"[blue bold]sudo cp {settings.SYSTEMD_SERVICE_SAVE_PATH} {settings.SYSTEMD_USER_SERVICE_PATH}"
        )
        print("[blue bold]sudo systemctl daemon-reload")
        print(f"[blue bold]sudo systemctl enable {settings.SYSTEMD_SERVICE_FILENAME}\n")
        print(f"[blue bold]sudo systemctl start {settings.SYSTEMD_SERVICE_FILENAME}\n")

        print("[green bold]Installation complete!")
        exit(0)

    @staticmethod
    def welcome_banner():
        os.system("sh scripts/banner.sh")

    @staticmethod
    def validate_input(text: str) -> bool:
        if text.strip().lower() == "y":
            return True
        return False

    def update_current_settings(self) -> bool:
        print("[green bold]Checking for existing settings...\n")

        current_settings = self.user_settings_manager.load_settings()

        if not current_settings:
            return True

        self.obsidian_vault_path = current_settings.obsidian_vault_path
        self.github_repo_url = current_settings.github_repo_url

        print("[red bold]Current settings found:\n")
        print(f"[yellow]Obsidian Vault Path: {self.obsidian_vault_path}")
        print(f"[yellow]GitHub Repo URL: {self.github_repo_url}\n")

        print("[red bold]Would you like to change these settings? (y/N): ", end="")
        user_input = input() or "N"

        if Installer.validate_input(user_input):
            return True

        return False

    def start_interactive_shell(self):
        print(
            f"[blue bold]Please enter the path to your Obsidian vault "
            f"[green]({settings.DEFAULT_VAULT_PATH})[blue bold]: ",
            end="",
        )
        obsidian_vault_path = input()

        if not obsidian_vault_path:
            obsidian_vault_path = settings.DEFAULT_VAULT_PATH

        self.obsidian_vault_path = obsidian_vault_path

        if not Path(self.obsidian_vault_path).exists():
            print(
                f"[red bold]The path {self.obsidian_vault_path} does not exist! "
                f"Please enter a valid path."
            )
            self.start_interactive_shell()

        print("[blue bold]Please enter the URL to your GitHub repository")
        print(
            "[blue bold]URL [green]with format: https://github.com/username/repo_name.git: ",
            end="",
        )
        github_repo_url = input()
        self.github_repo_url = github_repo_url

        print("\n")
        print("[red bold]Please confirm your settings:\n")
        print(f"[yellow]Obsidian Vault Path: {self.obsidian_vault_path}")
        print(f"[yellow]GitHub Repo URL: {self.github_repo_url}\n")
        print("[blue bold]Is this correct? (Y/n): ", end="")
        user_input = input()
        if not user_input:
            user_input = "Y"
        confirmation = Installer.validate_input(user_input)
        if confirmation:
            self.install()
        else:
            print("[yellow]Installation cancelled.")
            exit(0)

    def install(self):
        user_settings = UserSettings(
            obsidian_vault_path=str(self.obsidian_vault_path),
            github_repo_url=self.github_repo_url,
        )
        self.user_settings_manager.save_settings(user_settings)
        print("[green bold]Settings saved successfully!\n")


if __name__ == "__main__":
    try:
        user_settings_manager = UserSettingsManager()
        Installer(user_settings_manager).start()
    except KeyboardInterrupt:
        print("\nInstallation cancelled.")
        exit(0)
