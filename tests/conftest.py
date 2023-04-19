from pathlib import Path

import pytest
from config import settings as _settings

ROOT = Path(__file__).parent.parent
ROOT_SETTINGS = ROOT / "settings.toml"
TEST_SETTINGS = ROOT / "tests" / "settings.toml"


@pytest.fixture(autouse=True)
def settings():
    _settings.load_file(path=[ROOT_SETTINGS, TEST_SETTINGS], silent=False)
    yield _settings
    _settings.clean()
