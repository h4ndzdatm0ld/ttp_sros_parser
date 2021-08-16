"""Test Helper Functions."""
from ttp_sros_parser.helpers import globfindfile, check_file
import pytest


def test_globfindfile_no_match():
    """Test Failure."""
    with pytest.raises(SystemExit) as exit_err:
        globfindfile(r"*.xyz")
    assert exit_err.value.code == "No *.xyz file found."


def test_check_file_success():
    """Test success."""
    res = check_file("tests/fixtures/configs/example-config-7750.txt")
    assert res == "tests/fixtures/configs/example-config-7750.txt"


def test_value_error():
    """Test fail wrong extension."""
    with pytest.raises(ValueError) as val_err:
        check_file("test.py")
    assert str(val_err.value) == "test.py must end with '.cfg', '.txt' or '.log'"


def test_sys_exit_no_path():
    """Test fail wrong path."""
    with pytest.raises(SystemExit) as sys_err:
        check_file("test/some_config.cfg")
    assert str(sys_err.value) == "test/some_config.cfg doesn't exist."
