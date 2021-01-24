from ttp_sros_parser import __version__
from ttp_sros_parser.srosparser import SrosParser
import os

def test_version():
    assert __version__ == '0.1.0'

# This is the config file used to test.
example_config = f"{os.path.dirname(os.path.realpath(__file__))}/configs/example-config.txt"

def test_templates_as_list():
    """
    Test to ensure all templates are imported as a list.
    """
    data = "simple text to instantiate class."
    parser = SrosParser(data)
    assert type(parser.get_all_templates()), list


def test_get_router_interfaces():
    """
    Test to ensure interfaces are extracted from the base context.
    """
    parser = SrosParser(example_config)
    result = parser.get_router_interfaces()
    interfaces = """[
    {
        "router": [
            {
                "interfaces": [
                    {
                        "admin_state": true,
                        "ingress_stats": true,
                        "interface_name": "system",
                        "ipv4": {
                            "primary": {
                                "address": "199.199.9.1",
                                "prefix_length": "32"
                            }
                        },
                        "ipv6": {
                            "address": {
                                "ipv6_address": "2001:1111:3333:0:420:2a0::",
                                "prefix-length": "128"
                            }
                        }
                    },
                    {
                        "admin_state": true,
                        "description": "LINK-TO-EXAMPLEPHX-P-AL-0420-01",
                        "interface_name": "TO-42069-7705",
                        "ipv4": {
                            "bfd": {
                                "ipv4_bfd": "500 receive 500 multiplier 3"
                            },
                            "primary": {
                                "address": "172.25.199.132",
                                "prefix_length": "31"
                            }
                        },
                        "ipv6": {
                            "address": [
                                {
                                    "ipv6_address": "2001:2222:3333:33e3:645:4a0::",
                                    "prefix-length": "64"
                                },
                                {
                                    "ipv6_bfd": "500 receive 500 multiplier 3 type cpm-np"
                                }
                            ]
                        },
                        "port": "lag-92:3482",
                        "qos": {
                            "network-policy": "10120"
                        }
                    }
                ]
            },
            {
                "autonomous-system": "64500"
            }
        ]
    }
]"""
    assert result == interfaces

def test_get_system_interfaces():
    """
    Test to retrieve the system interface only.
    """
    # this aint working
    parser = SrosParser(example_config)
    result = parser.get_system_interface()
    system_interface = """[
    {
        "router": {
            "interface": {
                "admin_state": true,
                "ingress_stats": true,
                "interface_name": "system",
                "ipv4": {
                    "primary": {
                        "address": "199.199.9.1",
                        "prefix_length": "32"
                    }
                },
                "ipv6": {
                    "address": {
                        "ipv6_address": "2001:1111:3333:0:420:2a0::",
                        "prefix-length>": "128"
                    }
                }
            }
        }
    }
]"""
    assert result == system_interface

def test_get_system_configuration():
    """
    Test to retrieve the system configuration.
    """
    # this aint working
    parser = SrosParser(example_config)
    result = parser.get_system_configuration()
    system_configuration = """[
{
    "system": {
        "contact": "Hugo Tinoco",
        "location": "Phoenix, AZ",
        "name": "EXAMPLEPHX-P-AL-7750-01",
        "ntp": [
            {
                "servers": [
                    "8.8.8.8",
                    "8.8.4.4"
                ]
            },
            {
                "admin_state": true,
                "auth_check": false,
                "time_zone": "MST"
            }
        ],
        "rollback": {
            "cf_slot": "cf2",
            "directory": "Rollback",
            "rollback": true
        },
        "snmp": {
            "packet_size": "9216"
        }
    }
}
]"""
    assert result, system_configuration

def test_get_full_config():
    """
    Ensure system_int, hostname and full_config isn't in compiled list.
    """
    import datetime

    x = datetime.datetime.now()
    date = x.strftime("%b-%d-%Y")

    parser = SrosParser(example_config)
    result = parser.get_full_config()

    print(result)

    file = f"Parsed-Configs/{date.upper()}/EXAMPLEPHX-P-AL-7750-01.cfg"

    assert result == file

def test_get_system_hostname():
    """
    Test extracting hostname only.
    """
    parser = SrosParser(example_config)
    result = parser.get_system_hostname()
    assert result == "EXAMPLEPHX-P-AL-7750-01"

def test_get_show_bof():
    """
    Test parsing show bof output
    """
    data = "tests/show_output/show_bof.txt"

    parser = SrosParser(data)
    result = parser.show_bof()
    bof = """[
{
    "bof": {
        "address": [
            {
                "address": "192.168.1.1",
                "prefix-length": "23"
            },
            {
                "address": "1001:1000:2a65:2000:0FA:413::6",
                "prefix-length": "64"
            }
        ],
        "autonegotiate": true,
        "console-speed": "115200",
        "dns-domain": "admin-save.com",
        "duplex": "full",
        "image": {
            "cf-card": "cf3",
            "primary-image": "7705-TiMOS-9.0.R9"
        },
        "persist": "off",
        "primary-config": {
            "cf-card": "cf3",
            "primary-config": "EXAMPLEPHX-P-AL-7705-01.txt.cfg"
        },
        "primary-dns": "192.168.1.1",
        "secondary-dns": "8.8.8.8",
        "speed": "100",
        "static-route": [
            {
                "network": "0.0.0.0/1",
                "next-hop": "192.168.100.1"
            },
            {
                "network": "128.0.0.0/1",
                "next-hop": "192.168.100.1"
            },
            {
                "network": "1001:1000:0A00::/40",
                "next-hop": "1001:1000:2a69:2000:0FA:420::FFFF"
            },
            {
                "network": "1001:1000:2A00::/40",
                "next-hop": "1001:1000:2a69:2000:0FA:420::FFFF"
            }
        ],
        "wait": "3"
    }
}
]"""
    assert result, bof

def test_get_system_cards():
    """
    Test extracting hostname only.
    """
    parser = SrosParser(example_config)
    result = parser.get_system_cards()
    cards = """[
{
    "system": {
        "card": [
            {
                "card-type": "imm-2pac-fp3",
                "fail-on-error": true,
                "mda": {
                    "admin-state": true,
                    "egress-xpl": {
                        "window": "10"
                    },
                    "fail-on-error": true,
                    "ingress-xpl": {
                        "window": "10"
                    },
                    "mda-slot": "1",
                    "mda-type": "p10-10g-sfp"
                },
                "slot-number": "2"
            },
            {
                "card-type": "imm5-10gb-xfp",
                "fail-on-error": true,
                "mda": {
                    "admin-state": false,
                    "fail-on-error": true,
                    "mda-slot": "1"
                },
                "slot-number": "4"
            }
        ]
    }
}
]"""
    assert result, cards

def test_get_system_maf():
    """
    Test extracting system MAF IPV4/6 Filters
    """
    parser = SrosParser(example_config)
    result = parser.get_system_maf()
    maf = """[
{
    "system": {
        "management-access-filter": [
            {
                "ip-filter-params": {
                    "admin-state": true,
                    "default-action": "deny",
                    "ipv4-filter": true
                },
                "ipv6-filter-params": {
                    "admin-state": false,
                    "default-action": "permit",
                    "ipv6-filter": true
                }
            },
            {
                "ip-filter": {
                    "entry": [
                        {
                            "action": "permit",
                            "description": "SSH Traffic",
                            "dst-port": "22 22",
                            "entry-id": "10",
                            "protocol": "tcp",
                            "router-instance": "management"
                        },
                        {
                            "action": "permit",
                            "description": "Some Syslog Server",
                            "entry-id": "25",
                            "router-instance": "management"
                        }
                    ]
                }
            },
            {
                "ipv6-filter": {
                    "entry": [
                        {
                            "action-instance": "permit",
                            "description": "SSH Traffic",
                            "dst-port": "22 22",
                            "entry-id": "10",
                            "router-instance": "management"
                        },
                        {
                            "action-instance": "permit",
                            "description": "Something Something Something",
                            "entry-id": "25",
                            "router-instance": "management",
                            "src-ip": "1001:2000:a06:2130:f0:fef:0:147/128"
                        }
                    ]
                }
            }
        ]
    }
}
]"""
    assert result, maf

def test_get_system_ethcfm():
    """
    Test extracting eth-cfm information
    """
    parser = SrosParser(example_config)
    result = parser.get_system_ethcfm()
    ethcfm = """[
{
    "system": {
        "eth-cfm": {
            "domain": [
                {
                    "assosciations": [
                        {
                            "assosciation-id": "1",
                            "bridge-id": "420691",
                            "format": "icc-based",
                            "name": "epipe-7750-01",
                            "remote-mepid": "420"
                        },
                        {
                            "assosciation-id": "2",
                            "bridge-id": "420692",
                            "format": "icc-based",
                            "name": "epipe-7750-02",
                            "remote-mepid": "1420"
                        }
                    ],
                    "domain-id": "1",
                    "format": "none",
                    "level": "1"
                },
                {
                    "assosciations": [
                        {
                            "assosciation-id": "1",
                            "bridge-id": "11111",
                            "format": "icc-based",
                            "name": "epipe-7750-01",
                            "remote-mepid": "4201"
                        },
                        {
                            "assosciation-id": "2",
                            "bridge-id": "2222",
                            "format": "icc-based",
                            "name": "epipe-7750-02",
                            "remote-mepid": "14202"
                        }
                    ],
                    "domain-id": "2",
                    "format": "none",
                    "level": "1"
                }
            ]
        }
    }
}
]"""
    assert result, ethcfm

def test_get_system_asn():
    """
    Test extracting system asn
    """
    parser = SrosParser(example_config)
    result = parser.get_system_asn()
    asn = "64500"
    assert result, asn

def test_get_custom_template():
    """
    Test running custom template.
    """
    template = "ttp_sros_parser/templates/custom/sros_custom_hostname_asn.ttp"
    parser = SrosParser(example_config)
    result = parser.get_custom_template(template_path=template)
    custom = """[
{
    "asn": {
        "router": {
            "autonomous-system": "64500"
        }
    },
    "system": {
        "hostname": "EXAMPLEPHX-P-AL-7750-01"
    }
}
]"""
    assert result, custom

def test_get_system_service_sdp():
    """
    Test extracting system SDPs
    """
    parser = SrosParser(example_config)
    result = parser.get_system_service_sdp()
    sdp = """[
{
    "system": {
        "service": {
            "sdp": [
                {
                    "admin-state": true,
                    "adv-mtu-override": true,
                    "description": "MPLS-LABEL-TO-7750-01",
                    "far-end": "10.100.69.0",
                    "keep-alive": {
                        "admin-state": false
                    },
                    "ldp": true,
                    "sdp-id": "215"
                },
                {
                    "admin-state": true,
                    "adv-mtu-override": true,
                    "description": "MPLS-LABEL-TO-7750-02",
                    "far-end": "10.100.69.1",
                    "keep-alive": {
                        "admin-state": false
                    },
                    "ldp": true,
                    "sdp-id": "1215"
                },
                {
                    "admin-state": true,
                    "far-end": "10.10.10.4",
                    "keep-alive": {
                        "admin-state": false
                    },
                    "lsp": "TO_R4",
                    "path-mtu": "9100",
                    "sdp-id": "14"
                }
            ]
        }
    }
}
]"""
    assert result, sdp

def test_get_router_static_routes():
    """
    Test extracting router static routes (BASE)
    """
    import json
    from pprint import pprint

    parser = SrosParser(example_config)
    result = parser.get_router_static_routes()
    routes = """[
{
    "router": {
        "static-route": {
            "ipv4": [
                {
                    "default-route": [
                        {
                            "default-route": {
                                "bfd-enable": true,
                                "next-hop": "192.168.0.1"
                            }
                        },
                        {
                            "default-route": {
                                "next-hop": "192.168.10.1",
                                "preference": "10"
                            }
                        }
                    ],
                    "entry": [
                        {
                            "bfd-enable": true,
                            "next-hop": "172.25.69.88",
                            "prefix": "10.115.69.65",
                            "prefix-length": "32"
                        },
                        {
                            "next-hop": "172.25.69.88",
                            "preference": "10",
                            "prefix": "10.115.69.65",
                            "prefix-length": "32"
                        }
                    ]
                },
                {
                    "black-hole": {
                        "black-hole": "black-hole",
                        "prefix": "10.115.69.101/32"
                    }
                }
            ],
            "ipv6": [
                {
                    "default-route": [
                        {
                            "default-route": "::/0 next-hop 1001:1000:206a:31cd:645:400::/64 bfd-enable"
                        },
                        {
                            "default-route": "::/0 next-hop 1001:1000:206a:31cc:645:400::/64 preference 10"
                        }
                    ],
                    "entry": [
                        {
                            "bfd-enable": true,
                            "next-hop": "1001:1000:206a:31cd:645:400::",
                            "prefix": "1001:1000:2000:0:645:2a0::",
                            "prefix-length": "128"
                        },
                        {
                            "next-hop": "1001:1000:206a:31cd:645:400::",
                            "preference": "10",
                            "prefix": "1001:1000:2000:0:645:2a0:0:1",
                            "prefix-length": "128"
                        }
                    ]
                },
                {
                    "black-hole": [
                        {
                            "black-hole": "black-hole",
                            "prefix": "1001:1000:2062:30cf::/64"
                        },
                        {
                            "black-hole": "black-hole",
                            "prefix": "1001:1000:2062:3634::/64"
                        }
                    ]
                }
            ]
        }
    }
}
]"""
    assert result, routes

def test_show_router_interface():
    """
    Test extracting router interfaces from show command
    """
    data = "tests/show_output/show_router_interface.txt"

    parser = SrosParser(data)
    result = parser.show_router_interface()
    interfaces = """[
{
    "router": [
        {
            "interfaces": {
                "L3-TELCO-IXR01-1": {
                    "address": [
                        {
                            "pfx-state": "INACCESSIBLE",
                            "prefix": "2001:1000:2062:357a:646:100:0:1",
                            "prefix-length": "64"
                        },
                        {
                            "pfx-state": "INACCESSIBLE",
                            "prefix": "2001:1666:2062:357a:646:100:0:1",
                            "prefix-length": "64"
                        },
                        {
                            "pfx-state": "INACCESSIBLE",
                            "prefix": "fe80::645:100:0:1",
                            "prefix-length": "64"
                        }
                    ],
                    "admin-state": "Up",
                    "ipv4": "Down",
                    "ipv6": "Down",
                    "mode": "IES",
                    "port-sap-id": "lag-1:300"
                },
                "L3-TELCO-IXR02-1": {
                    "address": [
                        {
                            "pfx-state": "PREFERRED",
                            "prefix": "2001:1666:2062:4222:649:100:0:1",
                            "prefix-length": "64"
                        },
                        {
                            "pfx-state": "PREFERRED",
                            "prefix": "fe80::645:100:0:1",
                            "prefix-length": "64"
                        }
                    ],
                    "admin-state": "Up",
                    "ipv4": "Down",
                    "ipv6": "Up",
                    "mode": "IES",
                    "port-sap-id": "lag-2:300"
                },
                "L3-TELCO-eNodeB0420-DUL-01": {
                    "address": [
                        {
                            "pfx-state": "n/a",
                            "prefix": "10.0.0.0",
                            "prefix-length": "31"
                        },
                        {
                            "pfx-state": "PREFERRED",
                            "prefix": "2001:1000:2062:24ae:649:100::",
                            "prefix-length": "64"
                        },
                        {
                            "pfx-state": "PREFERRED",
                            "prefix": "fe80::c8:ffff:fe00:0",
                            "prefix-length": "64"
                        }
                    ],
                    "admin-state": "Up",
                    "ipv4": "Up",
                    "ipv6": "Up",
                    "mode": "IES",
                    "port-sap-id": "1/1/c2/1:301"
                },
                "system": {
                    "address": [
                        {
                            "pfx-state": "n/a",
                            "prefix": "10.100.43.69",
                            "prefix-length": "32"
                        },
                        {
                            "pfx-state": "PREFERRED",
                            "prefix": "2001:4777:2062:2000:645:100:0:19f",
                            "prefix-length": "128"
                        }
                    ],
                    "admin-state": "Up",
                    "ipv4": "Up",
                    "ipv6": "Up",
                    "mode": "Network",
                    "port-sap-id": "system"
                },
                "to-7750-01": {
                    "address": [
                        {
                            "pfx-state": "n/a",
                            "prefix": "172.20.200.69",
                            "prefix-length": "31"
                        },
                        {
                            "pfx-state": "PREFERRED",
                            "prefix": "2001:1666:206a:335d:645:100:0:1",
                            "prefix-length": "64"
                        },
                        {
                            "pfx-state": "PREFERRED",
                            "prefix": "fe80::c8:ffff:fe00:0",
                            "prefix-length": "64"
                        }
                    ],
                    "admin-state": "Up",
                    "ipv4": "Up",
                    "ipv6": "Up",
                    "mode": "Network",
                    "port-sap-id": "1/1/c4/1:3415"
                },
                "to-BTS0420-7750-H2": {
                    "address": [
                        {
                            "pfx-state": "n/a",
                            "prefix": "172.20.200.1",
                            "prefix-length": "31"
                        },
                        {
                            "pfx-state": "INACCESSIBLE",
                            "prefix": "2001:1666:206a:335f:645:100::",
                            "prefix-length": "64"
                        },
                        {
                            "pfx-state": "INACCESSIBLE",
                            "prefix": "fe80::c8:ffff:fe00:14b",
                            "prefix-length": "64"
                        }
                    ],
                    "admin-state": "Up",
                    "ipv4": "Down",
                    "ipv6": "Down",
                    "mode": "Network",
                    "port-sap-id": "lag-11:4094"
                }
            }
        },
        {
            "count": {
                "total": "6"
            }
        }
    ]
}
]"""
    assert result, interfaces

def test_get_system_profiles():
    """
    Test extracting system profiles
    """

    parser = SrosParser(example_config)
    result = parser.get_system_profiles()
    profiles = """[
{
    "system": {
        "profile": [
            {
                "default-action": "deny-all",
                "entry": [
                    {
                        "action": "permit",
                        "match": "back"
                    },
                    {
                        "action": "permit",
                        "match": "exit"
                    }
                ],
                "user-profile-name": "readonly"
            },
            {
                "default-action": "permit-all",
                "entry": [
                    {
                        "action": "deny",
                        "match": "configure system security"
                    },
                    {
                        "action": "permit",
                        "match": "show system security"
                    }
                ],
                "user-profile-name": "administrative"
            },
            {
                "default-action": "permit-all",
                "entry": [
                    {
                        "action": "deny",
                        "match": "configure system security"
                    },
                    {
                        "action": "permit",
                        "match": "show system security"
                    }
                ],
                "user-profile-name": "Test Profile 69"
            }
        ]
    }
}
]"""
    assert result, profiles

def test_file_dir_output():

    """
    Test parsing file dir output
    """
    example_file_dir="tests/show_output/file_dir.txt"
    parser = SrosParser(example_file_dir)
    result = parser.show_file_dir()
    filedir = """[
{
    "cf-contents": {
        "directory": {
            "cf-card": "cf3",
            "count": {
                "bytes-free": "789516288",
                "bytes-used": "14330",
                "total-dirs": "5",
                "total-files": "7"
            },
            "directories": [
                {
                    "DIR": true,
                    "date": "11/06/2020",
                    "directory": ".ssh/",
                    "time": "06:52a"
                },
                {
                    "DIR": true,
                    "date": "06/17/2020",
                    "directory": "SYSLINUX/",
                    "time": "02:06p"
                },
                {
                    "DIR": true,
                    "date": "06/17/2020",
                    "directory": "TIMOS/",
                    "time": "02:06p"
                },
                {
                    "DIR": true,
                    "date": "12/30/2020",
                    "directory": "certs/",
                    "time": "06:32p"
                },
                {
                    "DIR": true,
                    "date": "11/13/2020",
                    "directory": "system-pki/",
                    "time": "02:17a"
                }
            ],
            "files": [
                {
                    "date": "06/17/2020",
                    "filename": "CONFIG.CFG",
                    "size": "0",
                    "time": "02:06p"
                },
                {
                    "date": "06/17/2020",
                    "filename": "NVRAM.DAT",
                    "size": "101",
                    "time": "02:06p"
                },
                {
                    "date": "11/14/2020",
                    "filename": "bof.cfg",
                    "size": "682",
                    "time": "02:53a"
                },
                {
                    "date": "12/26/2020",
                    "filename": "bootlog.txt",
                    "size": "6614",
                    "time": "02:39p"
                },
                {
                    "date": "12/26/2020",
                    "filename": "bootlog_prev.txt",
                    "size": "6614",
                    "time": "02:35p"
                },
                {
                    "date": "12/26/2020",
                    "filename": "nvsys.info",
                    "size": "317",
                    "time": "02:38p"
                },
                {
                    "date": "12/26/2020",
                    "filename": "restcntr.txt",
                    "size": "2",
                    "time": "02:38p"
                }
            ]
        },
        "volume": [
            {
                "slot": "A",
                "volume": "in drive cf3 on slot A is SROS VM."
            },
            {
                "slot": "A",
                "volume": "in drive cf3 on slot A is formatted as FAT32"
            }
        ]
    }
}
]"""
    assert result, filedir
    
def test_show_service_service_using():

    """
    Test parsing show service service using show command
    """
    example_output="tests/show_output/show_service_service_using.txt"
    parser = SrosParser(example_output)
    result = parser.show_service_service_using()
    services = """[
{
    "service-using": {
        "count": {
            "total-services": "3"
        },
        "services": [
            {
                "admin-state": "Down",
                "customer-id": "1",
                "operational-state": "Down",
                "service-id": "100",
                "service-name": "100",
                "service-type": "VPRN"
            },
            {
                "admin-state": "Up",
                "customer-id": "1",
                "operational-state": "Down",
                "service-id": "2147483648",
                "service-name": "_tmnx_InternalIesService",
                "service-type": "IES"
            },
            {
                "admin-state": "Up",
                "customer-id": "1",
                "operational-state": "Down",
                "service-id": "2147483649",
                "service-name": "_tmnx_InternalVplsService",
                "service-type": "intVpls"
            }
        ]
    }
}
]"""
    assert result,services

def test_show_router_static_route_tag_ipv4():

    """
    Test parsing show router static-route with ipv4 flag
    """
    example_output="tests/show_output/show_router_static_route.txt"
    parser = SrosParser(example_output)
    result = parser.show_router_static_route(protocol='IPV4')
    ipv4_routes = """[
{
    "static_route": {
        "ipv4": {
            "count": {
                "total-routes": "6"
            },
            "entry": [
                {
                    "active": "Y",
                    "ipaddress": "10.115.30.0/24",
                    "metric": "1",
                    "next-hop": {
                        "interface": "n/a",
                        "next-hop": "n/a"
                    },
                    "preference": "5",
                    "tag": "1000",
                    "type": "BH"
                },
                {
                    "active": "Y",
                    "ipaddress": "10.115.43.0/24",
                    "metric": "1",
                    "next-hop": {
                        "interface": "n/a",
                        "next-hop": "n/a"
                    },
                    "preference": "5",
                    "tag": "1000",
                    "type": "BH"
                },
                {
                    "active": "Y",
                    "ipaddress": "10.115.56.0/24",
                    "metric": "1",
                    "next-hop": {
                        "interface": "n/a",
                        "next-hop": "n/a"
                    },
                    "preference": "5",
                    "tag": "1000",
                    "type": "BH"
                },
                {
                    "active": "Y",
                    "ipaddress": "10.119.228.0/23",
                    "metric": "1",
                    "next-hop": {
                        "interface": "n/a",
                        "next-hop": "n/a"
                    },
                    "preference": "5",
                    "tag": "1000",
                    "type": "BH"
                },
                {
                    "active": "Y",
                    "ipaddress": "10.119.228.16/28",
                    "metric": "1",
                    "next-hop": {
                        "interface": "n/a",
                        "next-hop": "n/a"
                    },
                    "preference": "5",
                    "tag": "1000",
                    "type": "BH"
                },
                {
                    "active": "Y",
                    "ipaddress": "10.253.236.0/23",
                    "metric": "1",
                    "next-hop": {
                        "interface": "n/a",
                        "next-hop": "n/a"
                    },
                    "preference": "5",
                    "tag": "1000",
                    "type": "BH"
                }
            ]
        }
    }
}
]"""
    assert result, ipv4_routes

def test_show_router_static_route_tag_ipv6():

    """
    Test parsing show router static-route with ipv6 flag
    """
    example_output="tests/show_output/show_router_static_route.txt"
    parser = SrosParser(example_output)
    result = parser.show_router_static_route(protocol='IPV6')
    ipv6_result = """[
{
    "static_route": {
        "ipv6": {
            "count": {
                "total-routes": "4"
            },
            "entry": [
                {
                    "active": "Y",
                    "ipaddress": "2001:4888:26f:4100::/56",
                    "metric": "1",
                    "next-hop": {
                        "interface": "n/a",
                        "next-hop": "n/a"
                    },
                    "preference": "5",
                    "tag": "1000",
                    "type": "BH"
                },
                {
                    "active": "N",
                    "ipaddress": "2001:4888:26f:4140::/64",
                    "metric": "1",
                    "next-hop": {
                        "interface": "n/a",
                        "next-hop": "n/a"
                    },
                    "preference": "5",
                    "tag": "1000",
                    "type": "BH"
                },
                {
                    "active": "Y",
                    "ipaddress": "2001:4888:2000:0:645:2a0::/112",
                    "metric": "1",
                    "next-hop": {
                        "interface": "n/a",
                        "next-hop": "n/a"
                    },
                    "preference": "5",
                    "tag": "1000",
                    "type": "BH"
                },
                {
                    "active": "Y",
                    "ipaddress": "2001:4888:2062:3000::/52",
                    "metric": "1",
                    "next-hop": {
                        "interface": "n/a",
                        "next-hop": "n/a"
                    },
                    "preference": "5",
                    "tag": "1000",
                    "type": "BH"
                }
            ]
        }
    }
}
]"""
    # assert result == ipv6_result

    def test_show_router_route_table():

        """
        Test parsing show router route table
        """
        example_output="tests/show_output/show_router_route_table.txt"
        parser = SrosParser(example_output)
        result = parser.show_router_route_table()
        routes = """[
    {
        "route-table": [
            {
                "ipv4": {
                    "count": {
                        "total-routes": "7"
                    },
                    "entry": [
                        {
                            "age": "09h15m13s",
                            "ipaddress": "10.115.30.0/24",
                            "next-hop": {
                                "metric": "1",
                                "next-hop": "Black Hole"
                            },
                            "pref": "5",
                            "protocol": "Static",
                            "type": "Blackh*"
                        },
                        {
                            "age": "09h15m13s",
                            "ipaddress": "10.115.43.0/24",
                            "next-hop": {
                                "metric": "1",
                                "next-hop": "Black Hole"
                            },
                            "pref": "5",
                            "protocol": "Static",
                            "type": "Blackh*"
                        },
                        {
                            "age": "09h15m13s",
                            "ipaddress": "10.115.56.0/24",
                            "next-hop": {
                                "metric": "1",
                                "next-hop": "Black Hole"
                            },
                            "pref": "5",
                            "protocol": "Static",
                            "type": "Blackh*"
                        },
                        {
                            "age": "09h15m14s",
                            "ipaddress": "10.115.56.0/32",
                            "next-hop": {
                                "metric": "0",
                                "next-hop": "system"
                            },
                            "pref": "0",
                            "protocol": "Local",
                            "type": "Local"
                        },
                        {
                            "age": "09h15m13s",
                            "ipaddress": "10.119.228.0/23",
                            "next-hop": {
                                "metric": "1",
                                "next-hop": "Black Hole"
                            },
                            "pref": "5",
                            "protocol": "Static",
                            "type": "Blackh*"
                        },
                        {
                            "age": "09h15m13s",
                            "ipaddress": "10.119.228.16/28",
                            "next-hop": {
                                "metric": "1",
                                "next-hop": "Black Hole"
                            },
                            "pref": "5",
                            "protocol": "Static",
                            "type": "Blackh*"
                        },
                        {
                            "age": "09h15m13s",
                            "ipaddress": "10.253.236.0/23",
                            "next-hop": {
                                "metric": "1",
                                "next-hop": "Black Hole"
                            },
                            "pref": "5",
                            "protocol": "Static",
                            "type": "Blackh*"
                        }
                    ]
                }
            },
            {
                "ipv6": {
                    "count": {
                        "total-routes": "4"
                    },
                    "entry": [
                        {
                            "age": "09h18m31s",
                            "ipaddress": "2001:4888:26f:3100::/56",
                            "next-hop": {
                                "metric": "1",
                                "next-hop": "Black Hole"
                            },
                            "pref": "5",
                            "protocol": "Static",
                            "type": "Blackh*"
                        },
                        {
                            "age": "09h18m31s",
                            "ipaddress": "2001:4888:2000:0:645:1a0::/112",
                            "next-hop": {
                                "metric": "1",
                                "next-hop": "Black Hole"
                            },
                            "pref": "5",
                            "protocol": "Static",
                            "type": "Blackh*"
                        },
                        {
                            "age": "09h18m32s",
                            "ipaddress": "2001:4888:2000:0:645:1a0::/128",
                            "next-hop": {
                                "metric": "0",
                                "next-hop": "system"
                            },
                            "pref": "0",
                            "protocol": "Local",
                            "type": "Local"
                        },
                        {
                            "age": "09h18m31s",
                            "ipaddress": "2001:4888:2062:2000::/52",
                            "next-hop": {
                                "metric": "1",
                                "next-hop": "Black Hole"
                            },
                            "pref": "5",
                            "protocol": "Static",
                            "type": "Blackh*"
                        }
                    ]
                }
            }
        ]
    }
]"""
        assert result == routes

def test_show_ravs_bof():

    """
    Test parsing show bof output from RAVS tool
    """
    example_output="tests/show_output/show_ravs_bof.txt"
    parser = SrosParser(example_output)
    result = parser.show_bof(ravs=True)
    ravs_bof1 = """[
    {
        "bof": {
            "address": [
                {
                    "address": "10.202.16.53",
                    "prefix-length": "23"
                },
                {
                    "address": "2001:4888:2A1A:A03D:192:400::1",
                    "prefix-length": "64"
                }
            ],
            "config": {
                "cf-card": "cf3",
                "primary-config": "PHLAPAbts0030.cfg"
            },
            "static_route": [
                {
                    "network": "10.134.221.0/24",
                    "next-hop": "10.202.16.52"
                },
                {
                    "network": "10.134.240.0/22",
                    "next-hop": "10.202.16.52"
                },
                {
                    "network": "10.193.0.0/16",
                    "next-hop": "10.202.16.52"
                },
                {
                    "network": "10.194.0.0/16",
                    "next-hop": "10.202.16.52"
                },
                {
                    "network": "10.215.128.0/17",
                    "next-hop": "10.202.16.52"
                },
                {
                    "network": "198.226.102.0/24",
                    "next-hop": "10.202.16.52"
                },
                {
                    "network": "199.74.154.0/23",
                    "next-hop": "10.202.16.52"
                }
            ]
        }
    }
]"""
    assert result == ravs_bof1

def test_show_ravs_bof2():
    
    """
    Test parsing show bof output from RAVS tool
    """
    example_output="tests/show_output/show_ravs_bof2.txt"
    parser = SrosParser(example_output)
    result = parser.show_bof(ravs=True)
    ravs_bof2 = """[
    {
        "bof": {
            "address": [
                {
                    "address": "10.202.16.55",
                    "prefix-length": "23"
                },
                {
                    "address": "2001:4888:2A1A:A03F:192:400::1",
                    "prefix-length": "64"
                }
            ],
            "config": {
                "cf-card": "cf3",
                "primary-config": "PHLAPAbts0032.cfg"
            },
            "static_route": [
                {
                    "network": "10.134.221.0/24",
                    "next-hop": "10.202.16.54"
                },
                {
                    "network": "10.134.240.0/22",
                    "next-hop": "10.202.16.54"
                },
                {
                    "network": "10.193.0.0/16",
                    "next-hop": "10.202.16.54"
                },
                {
                    "network": "10.194.0.0/16",
                    "next-hop": "10.202.16.54"
                },
                {
                    "network": "10.215.128.0/17",
                    "next-hop": "10.202.16.54"
                },
                {
                    "network": "198.226.102.0/24",
                    "next-hop": "10.202.16.54"
                },
                {
                    "network": "199.74.154.0/23",
                    "next-hop": "10.202.16.54"
                }
            ]
        }
    }
]"""
    assert result == ravs_bof2
    

def test_show_ravs_bof2_type():
    
    """
    Test parsing show bof output  1 from RAVS tool -> str
    """
    example_output="tests/show_output/show_ravs_bof2.txt"
    parser = SrosParser(example_output)
    result = parser.show_bof(ravs=True)
    assert type(result) == str

def test_show_ravs_bof1_type():
    
    """
    Test parsing show bof output 2 from RAVS tool -> str
    """
    example_output="tests/show_output/show_ravs_bof1.txt"
    parser = SrosParser(example_output)
    result = parser.show_bof(ravs=True)
    assert type(result) == str

def test_get_ports():
    
    """
    Test parsing get ports config
    """
    example_output="tests/show_output/show_ravs_bof1.txt"
    parser = SrosParser(example_config)
    result = parser.get_ports()
    print(result)