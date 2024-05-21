from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="config/.env", env_prefix="OBSIDIAN_SYNC_"
    )

    ROOT_PATH: Path = Path(__file__).parent.parent.resolve()
    CONFIG_PATH: Path = ROOT_PATH / "config"
    USER_CONFIG_PATH: Path = CONFIG_PATH / "user_settings.json"
    HOME_PATH: Path = Path.home()
    DEFAULT_VAULT_PATH: Path = HOME_PATH / "Obsidian" / "Vault"

    SYSTEMD_SERVICE_FILENAME: str = "obsidian_sync.service"
    SYSTEMD_USER_SERVICE_PATH: Path = Path(
        f"/etc/systemd/system/{SYSTEMD_SERVICE_FILENAME}"
    )
    SYSTEMD_SERVICE_SAVE_PATH: Path = ROOT_PATH / "systemd" / SYSTEMD_SERVICE_FILENAME


settings = Settings()
