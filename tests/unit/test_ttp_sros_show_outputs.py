"""Test show command output parsing."""
from ttp_sros_parser.srosparser import SrosParser


def test_get_show_bof(sros_parser, parsed_show_bof):
    """Test parsing show bof output."""
    data = "tests/fixtures/show_output/show_bof.txt"

    sros_parser = SrosParser(data)
    result = sros_parser.show_bof()
    assert result == parsed_show_bof
