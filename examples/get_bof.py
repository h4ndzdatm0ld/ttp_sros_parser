"""Get Bof Example."""
import json
from pprint import pprint
from ttp_sros_parser.srosparser import SrosParser

EXAMPLE_CONFIG = "tests/example-config.txt"

router = SrosParser(EXAMPLE_CONFIG)

data = router.get_router_interfaces()

interfaces = json.loads(data)

pprint(interfaces)
