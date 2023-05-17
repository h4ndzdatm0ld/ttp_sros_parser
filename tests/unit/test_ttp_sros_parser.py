"""Test SROS Parser."""
# from ttp_sros_parser import __version__


# def test_version():
#     assert __version__ == "0.1.5"


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


def test_get_system_begin(sros_parser, parsed_system_begin):
    """
    Test to retrieve the system begin configuration.
    """
    result = sros_parser.get_system_begin()
    assert result == parsed_system_begin


def test_get_mgmt_router_config(sros_parser, parsed_mgmt_router_config):
    """
    Test to retrieve the management router configuration.
    """
    result = sros_parser.get_mgmt_router_config()
    assert result == parsed_mgmt_router_config


def test_get_cflowd(sros_parser, parsed_cflowd):
    """
    Test to retrieve the cflowd configuration.
    """
    result = sros_parser.get_cflowd()
    assert result == parsed_cflowd


def test_get_filter_log_configuration(sros_parser, parsed_filter_log_configuration):
    """
    Test to retrieve the filter log configuration.
    """
    result = sros_parser.get_filter_log_configuration()
    assert result == parsed_filter_log_configuration


def test_get_filter_match_list_configuration(sros_parser, parsed_filter_match_list_configuration):
    """
    Test to retrieve the filter match list configuration.
    """
    result = sros_parser.get_filter_match_list_configuration()
    assert result == parsed_filter_match_list_configuration


def test_get_system_security_configuration(sros_parser, parsed_system_security_configuration):
    """
    Test to retrieve the system security configuration.
    """
    result = sros_parser.get_system_security_configuration()
    assert result == parsed_system_security_configuration


def test_get_qos_policy_configuration(sros_parser, parsed_qos_policy_configuration):
    """
    Test to retrieve the qos policy configuration.
    """
    result = sros_parser.get_qos_policy_configuration()
    assert result == parsed_qos_policy_configuration


def test_get_qos_policy_configuration1(sros_parser, parsed_qos_policy_configuration1):
    """
    Test to retrieve the qos policy configuration 1.
    """
    result = sros_parser.get_qos_policy_configuration1()
    assert result == parsed_qos_policy_configuration1


def test_get_qos_policy_configuration2(sros_parser, parsed_qos_policy_configuration2):
    """
    Test to retrieve the qos policy configuration 2.
    """
    result = sros_parser.get_qos_policy_configuration2()
    assert result == parsed_qos_policy_configuration2


def test_get_isis_configuration(sros_parser, parsed_isis_configuration):
    """
    Test to retrieve the ISIS configuration.
    """
    result = sros_parser.get_isis_configuration()
    assert result == parsed_isis_configuration


def test_get_subscriber_mgmt_configuration(sros_parser, parsed_subscriber_mgmt_configuration):
    """
    Test to retrieve the subscriber management configuration.
    """
    result = sros_parser.get_subscriber_mgmt_configuration()
    assert result == parsed_subscriber_mgmt_configuration


def test_get_aaa_declarations_configuration(sros_parser, parsed_aaa_declarations_configuration):
    """
    Test to retrieve the AAA declarations configuration.
    """
    result = sros_parser.get_aaa_declarations_configuration()
    assert result == parsed_aaa_declarations_configuration


def test_get_multicast_path_management_policy_configuration(
    sros_parser, parsed_multicast_path_management_policy_configuration
):
    """
    Test to retrieve the multicast path management policy configuration.
    """
    result = sros_parser.get_multicast_path_management_policy_configuration()
    assert result == parsed_multicast_path_management_policy_configuration


def test_get_port_xc_configuration(sros_parser, parsed_port_xc_configuration):
    """
    Test to retrieve the port xc configuration.
    """
    result = sros_parser.get_port_xc_configuration()
    assert result == parsed_port_xc_configuration


def test_get_redundancy_configuration(sros_parser, parsed_redundancy_configuration):
    """
    Test to retrieve the redundancy configuration.
    """
    result = sros_parser.get_redundancy_configuration()
    assert result == parsed_redundancy_configuration


def test_get_filter_configuration(sros_parser, parsed_filter_configuration):
    """
    Test to retrieve the filter configuration.
    """
    result = sros_parser.get_filter_configuration()
    assert result == parsed_filter_configuration


def test_get_vrrp_configuration(sros_parser, parsed_vrrp_configuration):
    """
    Test to retrieve the VRRP configuration.
    """
    result = sros_parser.get_vrrp_configuration()
    assert result == parsed_vrrp_configuration


def test_get_igmp_configuration(sros_parser, parsed_igmp_configuration):
    """
    Test to retrieve the IGMP configuration.
    """
    result = sros_parser.get_igmp_configuration()
    assert result == parsed_igmp_configuration


def test_get_l2tp_configuration(sros_parser, parsed_l2tp_configuration):
    """
    Test to retrieve the L2TP configuration.
    """
    result = sros_parser.get_l2tp_configuration()
    assert result == parsed_l2tp_configuration


def test_get_router_policy_configuration(sros_parser, parsed_router_policy_configuration):
    """
    Test to retrieve the router policy configuration.
    """
    result = sros_parser.get_router_policy_configuration()
    assert result == parsed_router_policy_configuration


def test_get_router_bgp_configuration(sros_parser, parsed_router_bgp_configuration):
    """
    Test to retrieve the router BGP configuration.
    """
    result = sros_parser.get_router_bgp_configuration()
    assert result == parsed_router_bgp_configuration


def test_get_subscriber_mgmt_ss_configuration(sros_parser, parsed_subscriber_mgmt_ss_configuration):
    """
    Test to retrieve the subscriber management SS configuration.
    """
    result = sros_parser.get_subscriber_mgmt_ss_configuration()
    assert result == parsed_subscriber_mgmt_ss_configuration


def test_get_mirror_configuration(sros_parser, parsed_mirror_configuration):
    """
    Test to retrieve the mirror configuration.
    """
    result = sros_parser.get_mirror_configuration()
    assert result == parsed_mirror_configuration


def test_get_radius_configuration(sros_parser, parsed_radius_configuration):
    """
    Test to retrieve the RADIUS configuration.
    """
    result = sros_parser.get_radius_configuration()
    assert result == parsed_radius_configuration


def test_get_dhcp_configuration(sros_parser, parsed_dhcp_configuration):
    """
    Test to retrieve the DHCP configuration.
    """
    result = sros_parser.get_dhcp_configuration()
    assert result == parsed_dhcp_configuration


def test_get_twamp_light_config(sros_parser, parsed_twamp_light_config):
    """
    Test to retrieve the TWAMP light configuration.
    """
    result = sros_parser.get_twamp_light_config()
    assert result == parsed_twamp_light_config


def test_get_aaa_configuration(sros_parser, parsed_aaa_configuration):
    """
    Test to retrieve the AAA configuration.
    """
    result = sros_parser.get_aaa_configuration()
    assert result == parsed_aaa_configuration


def test_get_pim_configuration(sros_parser, parsed_pim_configuration):
    """
    Test to retrieve the PIM configuration.
    """
    result = sros_parser.get_pim_configuration()
    assert result == parsed_pim_configuration


def test_get_ldp_configuration(sros_parser, parsed_ldp_configuration):
    """
    Test to retrieve the LDP configuration.
    """
    result = sros_parser.get_ldp_configuration()
    assert result == parsed_ldp_configuration


def test_get_system_time_ntp_config(sros_parser, parsed_system_time_ntp_config):
    """
    Test to retrieve the system time NTP configuration.
    """
    result = sros_parser.get_system_time_ntp_config()
    assert result == parsed_system_time_ntp_config
