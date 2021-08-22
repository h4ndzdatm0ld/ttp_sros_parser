"""Test SROS Parser."""
from ttp_sros_parser import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_templates_as_list(sros_parser):
    """
    Test to ensure all templates are imported as a list.
    """
    assert isinstance(sros_parser._get_all_templates(), list)


def test_get_router_interfaces(sros_parser, parsed_interfaces):
    """
    Test to ensure interfaces are extracted from the base context.
    """
    result = sros_parser.get_router_interfaces()
    assert result == parsed_interfaces


def test_get_system_interfaces(sros_parser, parsed_system_interface):
    """
    Test to retrieve the system interface only.
    """
    result = sros_parser.get_system_interface()
    assert result == parsed_system_interface


def test_get_system_configuration(sros_parser, parsed_system_configuration):
    """
    Test to retrieve the system configuration.
    """
    result = sros_parser.get_system_configuration()
    assert result == parsed_system_configuration


def test_get_full_config(sros_parser):
    """A full config top level keys."""
    result = sros_parser.get_full_config()
    assert [keys for keys in result[0].keys()] == ["configure", "router", "system"]


def test_get_system_hostname(sros_parser):
    """Test extracting hostname only."""
    result = sros_parser.get_system_hostname()
    assert result == "EXAMPLEPHX-P-AL-7750-01"


def test_get_system_cards(sros_parser, parsed_system_cards):
    """Test parsing system cards."""
    result = sros_parser.get_system_cards()
    assert result == parsed_system_cards


def test_get_system_maf(sros_parser, parsed_system_maf):
    """Test extracting system MAF IPV4/6 Filters."""
    result = sros_parser.get_system_maf()
    assert result == parsed_system_maf


def test_get_system_ethcfm(sros_parser, parsed_ethcfm):
    """
    Test extracting eth-cfm information
    """
    result = sros_parser.get_system_ethcfm()
    assert result == parsed_ethcfm


def test_get_system_asn(sros_parser):
    """
    Test extracting system asn
    """
    result = sros_parser.get_system_asn()
    assert result == "64500"


def test_get_custom_template(sros_parser):
    """
    Test running custom template.
    """
    template = "ttp_sros_parser/templates/custom/sros_custom_hostname_asn.ttp"
    result = sros_parser.get_custom_template(template_path=template)
    custom = [{"asn": {"router": {"autonomous-system": "64500"}}, "system": {"hostname": "EXAMPLEPHX-P-AL-7750-01"}}]
    assert result == custom


def test_get_system_service_sdp(sros_parser, parsed_system_sdp):
    """
    Test extracting system SDPs
    """
    result = sros_parser.get_system_service_sdp()
    assert result, parsed_system_sdp


def test_get_router_static_routes(sros_parser, parsed_static_routes):
    """
    Test extracting router static routes (BASE)
    """
    result = sros_parser.get_router_static_routes()
    assert result == parsed_static_routes


def test_get_system_profiles(sros_parser, parsed_system_profiles):
    """
    Test extracting system profiles
    """
    result = sros_parser.get_system_profiles()
    assert result == parsed_system_profiles


def test_get_ports(sros_parser, parsed_ports):
    """
    Test parsing get ports config
    """
    result = sros_parser.get_ports()
    assert result == parsed_ports


def test_get_log_configuration(sros_parser, parsed_log):

    """
    Test parsing log configuration
    """
    result = sros_parser.get_log_configuration()
    result == parsed_log
