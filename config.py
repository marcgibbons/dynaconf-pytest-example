from pathlib import Path

from dynaconf import Dynaconf  # type: ignore

settings = Dynaconf(
    root_path=Path(__file__).parent,
    settings_files=["settings.toml"],
)
