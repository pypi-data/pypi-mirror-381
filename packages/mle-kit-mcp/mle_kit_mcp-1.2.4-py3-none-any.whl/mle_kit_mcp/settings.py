from __future__ import annotations

from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


_DEFAULT_WORKSPACE_DIR: Path = Path(__file__).parent / "workdir"


class Settings(BaseSettings):
    WORKSPACE_DIR: Optional[str] = None
    PORT: int = 5057

    GPU_TYPE: str = "RTX_3090"
    DISK_SPACE: int = 300
    EXISTING_INSTANCE_ID: Optional[int] = None
    EXISTING_SSH_KEY: Optional[str] = None
    VAST_AI_KEY: Optional[str] = None

    OPENROUTER_API_KEY: str = ""
    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
