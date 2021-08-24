[![codecov](https://codecov.io/gh/h4ndzdatm0ld/ttp_sros_parser/branch/main/graph/badge.svg?token=ZL8JDKLQJI)](https://codecov.io/gh/h4ndzdatm0ld/ttp_sros_parser)

# TTP SrosParser

A library to parse a Nokia SROS 7750 full hierarchical configuration text file into structured data. Show commands are also able to be parsed, if included in the file alongside the configuration. This library is still under development, but a lot of parsers are readily available (see below for supported features). Configurations used for testing have all been on release version higher than TiMOS 16. At the moment, there is no capability to specify release version to accommodate different parsing templates.

## What TTP SrosParser is not

A library that connects and extracts information from a remote device. You, as the end-user must obtain a text file of the configuration. This file will be passed into the SrosParser class and you are able to convert a flat text configuration file into structure data using the built-in TTP parser templates. At this point, it's recommended to use a new instance of the srosparser with an individual show command as the text to parse to get the best results when parsing a show commands.

## Example

```python
"""SrosParser - Example."""
from ttp_sros_parser.srosparser import SrosParser

EXAMPLE_CONFIG = "some/dir/path/to/7750-config.txt"

# Instantiate class
router = SrosParser(EXAMPLE_CONFIG)

# Call `get_system_cards` method
router.get_system_cards()
```

Results:

```json
[
   {
      "configure":{
         "card":{
            "card-type":{
               "card-type":"iom-1",
               "subscription-level":"cr"
            },
            "fail-on-error":true,
            "mda":{
               "admin-state":true,
               "egress-xpl":{
                  "window":"10"
               },
               "fail-on-error":true,
               "ingress-xpl":{
                  "window":"10"
               },
               "mda-slot":"1",
               "mda-type":"me6-100gb-qsfp28"
            },
            "slot-number":"1"
         }
      }
   }
]
```

## Available Methods (Parsers)

Current methods available (Automatically updated at build):

[Methods](docs/methods.md)

## Full Config

**SrosParser** allows you to parse the full configuration with a single method call, `get_full_config()` and receive the full JSON output of the device.

## Custom Templates

SrosParser allows you to simply specify a custom template after you initialize a new class object.

```python
router = SrosParser("path/to/config.txt")

cool_ttp_template = router.get_custom_template("path/to/template")

print(cool_ttp_template)
```

## Contributing

Any contribution to the project must include unit tests and pass all linting.

Simply run:

- `docker-compose build`
- `docker-compose run test`
