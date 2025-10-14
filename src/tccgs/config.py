"""Global config options of the package."""

import os
from importlib import resources as pkg_resources
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

PACKAGE_NAME = __package__

with pkg_resources.as_file(pkg_resources.files(PACKAGE_NAME)) as package_dir:
    DEFAULT_CONFIG_FILE_PATH = package_dir / "logger_config.toml"

LOGGER_CONFIG_FILE = Path(
    os.environ.get(f"{PACKAGE_NAME.replace('-', '_').upper()}_LOGGER_CONFIG_FILE", DEFAULT_CONFIG_FILE_PATH)
)
