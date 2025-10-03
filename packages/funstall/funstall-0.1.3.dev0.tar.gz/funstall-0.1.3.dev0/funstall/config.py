from enum import StrEnum
from pathlib import Path

from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

from funstall import system_paths


class Verbosity(StrEnum):
    SILENT = "silent"
    ERROR = "error"
    INFO = "info"
    DEBUG = "debug"


class Settings(BaseSettings):
    package_file_url: HttpUrl = HttpUrl(
        "https://raw.githubusercontent.com/"
        "hbibel/funstall/refs/heads/main/packages.yaml"
    )
    base_installation_dir: Path = system_paths.user_data_dir() / "packages"
    package_definitions_file: Path = (
        system_paths.user_data_dir() / "packages.yaml"
    )
    verbosity: Verbosity = Verbosity.ERROR

    model_config = SettingsConfigDict(
        yaml_file=system_paths.user_config_file_dir() / "config.yaml"
    )
