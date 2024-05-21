import json
from obsidian_sync.user_settings import UserSettings, UserSettingsManager
from obsidian_sync.config import settings


def test_user_settings_manager_save_settings():
    user_settings_manager = UserSettingsManager()
    user_settings = UserSettings(
        obsidian_vault_path="path/to/obsidian/vault",
        github_repo_url="https://test.com/repo.git",
    )
    user_settings_manager.save_settings(user_settings)

    json.loads(settings.USER_CONFIG_PATH.read_text()) == {
        "obsidian_vault_path": "path/to/obsidian/vault",
        "github_repo_url": "https://test.com/repo.git",
    }


def test_user_settings_manager_load_settings():
    user_settings_manager = UserSettingsManager()
    user_settings = UserSettings(
        obsidian_vault_path="path/to/obsidian/vault",
        github_repo_url="https://test.com/repo.git",
    )
    user_settings_manager.save_settings(user_settings)
    
    loaded_user_settings = user_settings_manager.load_settings()
    assert loaded_user_settings == user_settings
