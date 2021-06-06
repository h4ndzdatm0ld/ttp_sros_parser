from ttp_sros_parser.srosparser import SrosParser
import json
from pprint import pprint

example_config = "tests/example-config.txt"

router = SrosParser(example_config)

data = router.get_router_interfaces()

interfaces = json.loads(data)

pprint(interfaces)
