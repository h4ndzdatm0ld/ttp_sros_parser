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
def full_parsed_config():
    return f"{FIXTURES}/configs/example-json.json"


@pytest.fixture(scope="session")
def sros_parser(sar_config):
    return SrosParser(sar_config)


@pytest.fixture(scope="session")
def parsed_interfaces():
    with open(f"{FIXTURES}/parsed_results/admin_display/interfaces.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_show_bof():
    with open(f"{FIXTURES}/parsed_results/show_cmds/show_bof.json") as f:
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
def parsed_system_profiles():
    with open(f"{FIXTURES}/parsed_results/admin_display/system_profiles.json") as f:
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
