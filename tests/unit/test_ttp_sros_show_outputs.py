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


def test_get_show_route_table(parsed_show_router_table):
    """Test general show router route table."""
    data = "tests/fixtures/show_output/show_route_table.txt"
    sros_parser = SrosParser(data)
    result = sros_parser.show_router_route_table()
    assert result == parsed_show_router_table


def test_get_show_router_static_route_v4(parsed_static_route_v4):
    """Test general show router static route."""
    data = "tests/fixtures/show_output/show_router_static_route_tag.txt"
    sros_parser = SrosParser(data)
    result = sros_parser.show_router_static_route(protocol="ipv4")
    assert result == parsed_static_route_v4


def test_get_show_router_static_route_v4_default(parsed_static_route_v4):
    """Test general show router static route, default v4 without protocol specified."""
    data = "tests/fixtures/show_output/show_router_static_route_tag.txt"
    sros_parser = SrosParser(data)
    result = sros_parser.show_router_static_route()
    assert result == parsed_static_route_v4


def test_get_show_router_static_route_v6(parsed_static_route_v6):
    """Test general show router static route, ipv6 specified."""
    data = "tests/fixtures/show_output/show_router_static_route_tag_v6.txt"
    sros_parser = SrosParser(data)
    result = sros_parser.show_router_static_route(protocol="IPV6")
    assert result == parsed_static_route_v6
