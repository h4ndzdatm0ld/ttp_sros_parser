"""Contest."""
import json
import os

import pytest

from ttp_sros_parser.srosparser import SrosParser

FIXTURES = os.environ.get("FIXTURE_DIR", "./tests/fixtures")

############################
# Alphabetical JSON fixtures


@pytest.fixture(scope="session")
def sar_config():
    return f"{FIXTURES}/configs/example-config-sar.txt"


@pytest.fixture(scope="session")
def config_7750():
    return f"{FIXTURES}/configs/example-config-7750.txt"


@pytest.fixture(scope="session")
def full_parsed_config():
    return f"{FIXTURES}/configs/example-json.json"


@pytest.fixture(scope="session")
def sros_parser(sar_config):
    return SrosParser(sar_config)


@pytest.fixture(scope="session")
def sros_parser_7750(config_7750):
    return SrosParser(config_7750)


@pytest.fixture(scope="session")
def sros_parser_7750_R3():
    return SrosParser(f"{FIXTURES}/configs/example-config-7750-r3.txt")


@pytest.fixture(scope="session")
def sros_parser_7750_R2():
    return SrosParser(f"{FIXTURES}/configs/example-config-7750-r2.txt")


@pytest.fixture(scope="session")
def parsed_interfaces():
    with open(f"{FIXTURES}/parsed_results/admin_display/interfaces.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_show_bof():
    with open(f"{FIXTURES}/parsed_results/show_cmds/show_bof.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_show_router_table():
    with open(f"{FIXTURES}/parsed_results/show_cmds/show_router_route_table.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_static_route_v4():
    with open(f"{FIXTURES}/parsed_results/show_cmds/show_static_route_v4.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_static_route_v6():
    with open(f"{FIXTURES}/parsed_results/show_cmds/show_static_route_v6.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_show_file_dir():
    with open(f"{FIXTURES}/parsed_results/show_cmds/file_dir.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_system_interface():
    with open(f"{FIXTURES}/parsed_results/admin_display/system_interface.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_log():
    with open(f"{FIXTURES}/parsed_results/admin_display/log.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_ports():
    with open(f"{FIXTURES}/parsed_results/admin_display/ports.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_lsps():
    with open(f"{FIXTURES}/parsed_results/admin_display/mpls_lsps.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_system_profiles():
    with open(f"{FIXTURES}/parsed_results/admin_display/system_profiles.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_lags():
    with open(f"{FIXTURES}/parsed_results/admin_display/lag.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_lags_1():
    with open(f"{FIXTURES}/parsed_results/admin_display/lag_1.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_show_service_using():
    with open(f"{FIXTURES}/parsed_results/show_cmds/show_service_service_using.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_system_cards():
    with open(f"{FIXTURES}/parsed_results/admin_display/system_cards.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_show_router_int():
    with open(f"{FIXTURES}/parsed_results/show_cmds/show_router_interface.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_system_sdp():
    with open(f"{FIXTURES}/parsed_results/admin_display/system_sdp.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_static_routes():
    with open(f"{FIXTURES}/parsed_results/admin_display/static_routes.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_ethcfm():
    with open(f"{FIXTURES}/parsed_results/admin_display/ethcfm.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_system_maf():
    with open(f"{FIXTURES}/parsed_results/admin_display/system_maf.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_system_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/system_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_connectors():
    with open(f"{FIXTURES}/parsed_results/admin_display/connectors.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_python_declaration():
    with open(f"{FIXTURES}/parsed_results/admin_display/python_declaration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_python_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/python_declaration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_system_begin():
    with open(f"{FIXTURES}/parsed_results/admin_display/system_begin.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_mgmt_router_config():
    with open(f"{FIXTURES}/parsed_results/admin_display/mgmt_router_config.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_cflowd():
    with open(f"{FIXTURES}/parsed_results/admin_display/cflowd.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_filter_log_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/filter_log_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_filter_match_list_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/filter_match_list_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_system_security_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/system_security_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_qos_policy_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/qos_policy_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_qos_policy_configuration1():
    with open(f"{FIXTURES}/parsed_results/admin_display/qos_policy_configuration1.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_qos_policy_configuration2():
    with open(f"{FIXTURES}/parsed_results/admin_display/qos_policy_configuration2.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_isis_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/isis_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_subscriber_mgmt_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/subscriber_mgmt_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_aaa_declarations_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/aaa_declarations_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_system_time_ntp_config():
    with open(f"{FIXTURES}/parsed_results/admin_display/system_time_ntp_config.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_multicast_path_management_policy_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/multicast_path_management_policy_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_port_xc_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/port_xc_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_redundancy_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/redundancy_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_filter_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/filter_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_vrrp_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/vrrp_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_igmp_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/igmp_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_l2tp_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/l2tp_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_router_policy_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/router_policy_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_router_bgp_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/router_bgp_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_subscriber_mgmt_ss_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/subscriber_mgmt_ss_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_mirror_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/mirror_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_radius_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/radius_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_dhcp_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/dhcp_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_twamp_light_config():
    with open(f"{FIXTURES}/parsed_results/admin_display/twamp_light_config.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_aaa_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/aaa_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_pim_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/pim_configuration.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_ldp_configuration():
    with open(f"{FIXTURES}/parsed_results/admin_display/ldp_configuration.json") as f:
        return json.load(f)
