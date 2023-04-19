from main import get_timezone


def test_get_timezone_returns_default_value():
    """
    Expect the value defined in root `settings.toml`, despite
    `DYNACONF_TIMEZONE` being set.
    """
    assert get_timezone() == "America/Toronto"


def test_get_env_name_returns_test_setting_value(settings):
    """
    Test that the value defined in `tests/settings.toml` overwites
    the "prod" settings value.
    """
    assert settings.ENV_NAME == "test"


def test_get_timezone_with_overriden_setting_value(settings):
    new_tz = "Europe/Paris"
    settings.TIMEZONE = new_tz
    assert get_timezone() == new_tz


def test_get_timezone_value_does_not_leak_from_previous_test(settings):
    assert get_timezone() == "America/Toronto"
