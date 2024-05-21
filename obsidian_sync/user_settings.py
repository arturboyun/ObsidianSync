from dataclasses import asdict, dataclass
import json
from obsidian_sync.config import settings


@dataclass
class UserSettings:
    obsidian_vault_path: str
    github_repo_url: str


class UserSettingsManager:
    @staticmethod
    def save_settings(user_settings: UserSettings):
        settings.USER_CONFIG_PATH.write_text(
            json.dumps(asdict(user_settings), indent=4)
        )

    @staticmethod
    def load_settings() -> UserSettings | None:
        if not settings.USER_CONFIG_PATH.exists():
            return None
        return UserSettings(**json.loads(settings.USER_CONFIG_PATH.read_text()))
