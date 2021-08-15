"""Test show command output parsing."""
from ttp_sros_parser.srosparser import SrosParser


def test_file_dir_output(parsed_show_file_dir):
    """
    Test parsing file dir output
    """
    data = "tests/fixtures/show_output/file_dir.txt"
    parser = SrosParser(data)
    result = parser.show_file_dir()
    assert result == parsed_show_file_dir


def test_get_show_bof(parsed_show_bof):
    """Test parsing show bof output."""
    data = "tests/fixtures/show_output/show_bof.txt"

    sros_parser = SrosParser(data)
    result = sros_parser.show_bof()
    assert result == parsed_show_bof


def test_show_router_interface(parsed_show_router_int):
    """
    Test extracting router interfaces from show command
    """
    data = "tests/fixtures/show_output/show_router_interface.txt"

    sros_parser = SrosParser(data)
    result = sros_parser.show_router_interface()
    assert result == parsed_show_router_int


def test_show_service_service_using(parsed_show_service_using):

    """
    Test parsing show service service using show command
    """
    example_output = "tests/fixtures/show_output/show_service_service_using.txt"
    parser = SrosParser(example_output)
    result = parser.show_service_service_using()

    assert result, parsed_show_service_using
