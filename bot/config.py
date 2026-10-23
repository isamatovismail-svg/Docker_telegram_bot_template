from pydantic import SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Bot tokeni (@BotFather dan olinadi)
    bot_token: SecretStr

    # Administrator Telegram ID lari (vergul bilan ajratilgan string yoki list)
    admin_ids: list[int] = []

    # Logging darajasi
    logging_level: str = "INFO"

    @field_validator("admin_ids", mode="before")
    @classmethod
    def parse_admin_ids(cls, v):
        """ADMIN_IDS=111,222 formatini [111, 222] listga o'girish"""
        if isinstance(v, str):
            if not v.strip():
                return []
            return [int(x.strip()) for x in v.split(",") if x.strip().isdigit()]
        return v

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


# Global konfiguratsiya obyekti
config = Settings()
