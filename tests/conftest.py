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
    with open(f"{FIXTURES}/parsed_results/interfaces.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_show_bof():
    with open(f"{FIXTURES}/parsed_results/show_bof.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_system_interface():
    with open(f"{FIXTURES}/parsed_results/system_interface.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_system_cards():
    with open(f"{FIXTURES}/parsed_results/system_cards.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def parsed_system_configuration():
    with open(f"{FIXTURES}/parsed_results/system_configuration.json") as f:
        return json.load(f)
