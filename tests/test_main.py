from main import get_timezone


def test_get_timezone_returns_default_value():
    """
    Expect the value defined in root `settings.toml`, despite
    `DYNACONF_TIMEZONE` being set as an environment variable.
    This value was set in `pytest.ini` using the pytest-env plugin.
    """
    assert get_timezone() == "America/Toronto"


def test_get_env_name_returns_test_setting_value(settings):
    """
    Test that the value defined in `tests/settings.toml` overwrites
    the value set in the root `settings.toml` file. This confirms
    that the fixture loads both settings files.
    """
    assert settings.ENV_NAME == "test"


def test_get_timezone_with_overriden_setting_value(settings):
    """
    Test that changing the setting value in this test makes functional
    changes to application code.
    """
    new_tz = "Europe/Paris"
    settings.TIMEZONE = new_tz
    assert get_timezone() == new_tz


def test_get_timezone_value_does_not_leak_from_previous_test(settings):
    """
    Test that the previous test value does not leak.
    """
    assert get_timezone() == "America/Toronto"
