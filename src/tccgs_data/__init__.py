"""Assets."""

import importlib.resources as pkg_resources

with pkg_resources.as_file(pkg_resources.files(None)) as data_dir:  # type: ignore  # noqa: PGH003
    BASE_DIR = data_dir

WINDOW_ICON = BASE_DIR / 'icon_ico.ico'
TSUKASA_GIF_FILE = BASE_DIR / 'tsukasa.gif'
THX_BUTTON = BASE_DIR / 'thanks_button.png'
