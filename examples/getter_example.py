"""SrosParser Example."""
from pprint import pprint
from ttp_sros_parser.srosparser import SrosParser

EXAMPLE_CONFIG = "tests/fixtures/configs/example-config-7750.txt"

router = SrosParser(EXAMPLE_CONFIG)

pprint(router.get_system_cards())
