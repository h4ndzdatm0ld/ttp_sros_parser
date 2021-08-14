"""Test Helper Functions."""
from ttp_sros_parser.helpers import globfindfile
import pytest


def test_globfindfile_no_match():
    """Test Failure."""
    with pytest.raises(SystemExit) as exit_err:
        globfindfile(r"*.xyz")
    assert exit_err.value.code == "No *.xyz file found."
