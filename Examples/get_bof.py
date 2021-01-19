from ttp_sros_parser.srosparser import SrosParser

example_config = "tests/example-config.txt"
example_bof = "tests/example-show-bof-cli.txt"

router = SrosParser(example_config)

data = router.show_bof(example_bof)

import json
from pprint import pprint

bof = json.loads(data)

pprint(bof)

