"""Contest."""
import pytest
import os
import json
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
