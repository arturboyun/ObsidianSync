import logging
from pathlib import Path
from time import sleep

from obsidian_sync.syncher import Syncher
from obsidian_sync.user_settings import UserSettingsManager
from obsidian_sync.watcher import Watcher

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user_settings_manager = UserSettingsManager()
user_settings = user_settings_manager.load_settings()

if not user_settings:
    raise FileNotFoundError("User settings not found! Run install.sh first.")

watcher = Watcher(Path(user_settings.obsidian_vault_path).resolve())
syncher = Syncher(
    Path(user_settings.obsidian_vault_path),
    user_settings.github_repo_url,
)


@watcher.on_startup
def on_startup():
    logger.info("Initial sync with remote repository...")
    syncher.sync()


@watcher.on_change
def update_repo():
    logger.info("Updates detected! Pushing to remote repository...")
    syncher.sync()


@watcher.on_shutdown
def on_shutdown():
    logger.info("Exiting... Pushing changes to remote repository...")
    syncher.sync()


if __name__ == "__main__":
    watcher.start()
