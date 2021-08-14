"""Test show command output parsing."""
from ttp_sros_parser.srosparser import SrosParser


def test_file_dir_output(parsed_show_file_dir):
    """
    Test parsing file dir output
    """
    data = "tests/fixtures/show_output/file_dir.txt"
    parser = SrosParser(data)
    result = parser.show_file_dir()
    assert result == parsed_show_file_dir


def test_get_show_bof(parsed_show_bof):
    """Test parsing show bof output."""
    data = "tests/fixtures/show_output/show_bof.txt"

    sros_parser = SrosParser(data)
    result = sros_parser.show_bof()
    assert result == parsed_show_bof


def test_show_router_interface(parsed_show_router_int):
    """
    Test extracting router interfaces from show command
    """
    data = "tests/fixtures/show_output/show_router_interface.txt"

    sros_parser = SrosParser(data)
    result = sros_parser.show_router_interface()
    assert result == parsed_show_router_int


# def test_show_ravs_bof():

#     """
#     Test parsing show bof output from RAVS tool
#     """
#     example_output = "tests/show_output/show_ravs_bof.txt"
#     parser = SrosParser(example_output)
#     result = parser.show_bof(ravs=True)
#     ravs_bof1 = """[
#     {
#         "bof": {
#             "address": [
#                 {
#                     "address": "10.202.16.53",
#                     "prefix-length": "23"
#                 },
#                 {
#                     "address": "2001:4888:2A1A:A03D:192:400::1",
#                     "prefix-length": "64"
#                 }
#             ],
#             "config": {
#                 "cf-card": "cf3",
#                 "primary-config": "PHLAPAbts0030.cfg"
#             },
#             "static_route": [
#                 {
#                     "network": "10.134.221.0/24",
#                     "next-hop": "10.202.16.52"
#                 },
#                 {
#                     "network": "10.134.240.0/22",
#                     "next-hop": "10.202.16.52"
#                 },
#                 {
#                     "network": "10.193.0.0/16",
#                     "next-hop": "10.202.16.52"
#                 },
#                 {
#                     "network": "10.194.0.0/16",
#                     "next-hop": "10.202.16.52"
#                 },
#                 {
#                     "network": "10.215.128.0/17",
#                     "next-hop": "10.202.16.52"
#                 },
#                 {
#                     "network": "198.226.102.0/24",
#                     "next-hop": "10.202.16.52"
#                 },
#                 {
#                     "network": "199.74.154.0/23",
#                     "next-hop": "10.202.16.52"
#                 }
#             ]
#         }
#     }
# ]"""
#     assert result == ravs_bof1


# def test_show_ravs_bof2():

#     """
#     Test parsing show bof output from RAVS tool
#     """
#     example_output = "tests/show_output/show_ravs_bof2.txt"
#     parser = SrosParser(example_output)
#     result = parser.show_bof(ravs=True)
#     ravs_bof2 = """[
#     {
#         "bof": {
#             "address": [
#                 {
#                     "address": "10.202.16.55",
#                     "prefix-length": "23"
#                 },
#                 {
#                     "address": "2001:4888:2A1A:A03F:192:400::1",
#                     "prefix-length": "64"
#                 }
#             ],
#             "config": {
#                 "cf-card": "cf3",
#                 "primary-config": "PHLAPAbts0032.cfg"
#             },
#             "static_route": [
#                 {
#                     "network": "10.134.221.0/24",
#                     "next-hop": "10.202.16.54"
#                 },
#                 {
#                     "network": "10.134.240.0/22",
#                     "next-hop": "10.202.16.54"
#                 },
#                 {
#                     "network": "10.193.0.0/16",
#                     "next-hop": "10.202.16.54"
#                 },
#                 {
#                     "network": "10.194.0.0/16",
#                     "next-hop": "10.202.16.54"
#                 },
#                 {
#                     "network": "10.215.128.0/17",
#                     "next-hop": "10.202.16.54"
#                 },
#                 {
#                     "network": "198.226.102.0/24",
#                     "next-hop": "10.202.16.54"
#                 },
#                 {
#                     "network": "199.74.154.0/23",
#                     "next-hop": "10.202.16.54"
#                 }
#             ]
#         }
#     }
# ]"""
#     assert result == ravs_bof2


# def test_show_ravs_bof2_type():

#     """
#     Test parsing show bof output  1 from RAVS tool -> str
#     """
#     example_output = "tests/show_output/show_ravs_bof2.txt"
#     parser = SrosParser(example_output)
#     result = parser.show_bof(ravs=True)
#     assert type(result) == str


# def test_show_ravs_bof1_type():

#     """
#     Test parsing show bof output 2 from RAVS tool -> str
#     """
#     example_output = "tests/show_output/show_ravs_bof1.txt"
#     parser = SrosParser(example_output)
#     result = parser.show_bof(ravs=True)
#     assert type(result) == str


# def test_show_service_service_using():

#     """
#     Test parsing show service service using show command
#     """
#     example_output = "tests/show_output/show_service_service_using.txt"
#     parser = SrosParser(example_output)
#     result = parser.show_service_service_using()
#     services = """[
# {
#     "service-using": {
#         "count": {
#             "total-services": "3"
#         },
#         "services": [
#             {
#                 "admin-state": "Down",
#                 "customer-id": "1",
#                 "operational-state": "Down",
#                 "service-id": "100",
#                 "service-name": "100",
#                 "service-type": "VPRN"
#             },
#             {
#                 "admin-state": "Up",
#                 "customer-id": "1",
#                 "operational-state": "Down",
#                 "service-id": "2147483648",
#                 "service-name": "_tmnx_InternalIesService",
#                 "service-type": "IES"
#             },
#             {
#                 "admin-state": "Up",
#                 "customer-id": "1",
#                 "operational-state": "Down",
#                 "service-id": "2147483649",
#                 "service-name": "_tmnx_InternalVplsService",
#                 "service-type": "intVpls"
#             }
#         ]
#     }
# }
# ]"""
#     assert result, services


# def test_show_router_static_route_tag_ipv4():

#     """
#     Test parsing show router static-route with ipv4 flag
#     """
#     example_output = "tests/show_output/show_router_static_route.txt"
#     parser = SrosParser(example_output)
#     result = parser.show_router_static_route(protocol="IPV4")
#     ipv4_routes = """[
# {
#     "static_route": {
#         "ipv4": {
#             "count": {
#                 "total-routes": "6"
#             },
#             "entry": [
#                 {
#                     "active": "Y",
#                     "ipaddress": "10.115.30.0/24",
#                     "metric": "1",
#                     "next-hop": {
#                         "interface": "n/a",
#                         "next-hop": "n/a"
#                     },
#                     "preference": "5",
#                     "tag": "1000",
#                     "type": "BH"
#                 },
#                 {
#                     "active": "Y",
#                     "ipaddress": "10.115.43.0/24",
#                     "metric": "1",
#                     "next-hop": {
#                         "interface": "n/a",
#                         "next-hop": "n/a"
#                     },
#                     "preference": "5",
#                     "tag": "1000",
#                     "type": "BH"
#                 },
#                 {
#                     "active": "Y",
#                     "ipaddress": "10.115.56.0/24",
#                     "metric": "1",
#                     "next-hop": {
#                         "interface": "n/a",
#                         "next-hop": "n/a"
#                     },
#                     "preference": "5",
#                     "tag": "1000",
#                     "type": "BH"
#                 },
#                 {
#                     "active": "Y",
#                     "ipaddress": "10.119.228.0/23",
#                     "metric": "1",
#                     "next-hop": {
#                         "interface": "n/a",
#                         "next-hop": "n/a"
#                     },
#                     "preference": "5",
#                     "tag": "1000",
#                     "type": "BH"
#                 },
#                 {
#                     "active": "Y",
#                     "ipaddress": "10.119.228.16/28",
#                     "metric": "1",
#                     "next-hop": {
#                         "interface": "n/a",
#                         "next-hop": "n/a"
#                     },
#                     "preference": "5",
#                     "tag": "1000",
#                     "type": "BH"
#                 },
#                 {
#                     "active": "Y",
#                     "ipaddress": "10.253.236.0/23",
#                     "metric": "1",
#                     "next-hop": {
#                         "interface": "n/a",
#                         "next-hop": "n/a"
#                     },
#                     "preference": "5",
#                     "tag": "1000",
#                     "type": "BH"
#                 }
#             ]
#         }
#     }
# }
# ]"""
#     assert result, ipv4_routes


# # def test_show_router_static_route_tag_ipv6():

# #     """
# #     Test parsing show router static-route with ipv6 flag
# #     """
# #     example_output = "tests/show_output/show_router_static_route.txt"
# #     parser = SrosParser(example_output)
# #     result = parser.show_router_static_route(protocol="IPV6")
# #     ipv6_result = """[
# # {
# #     "static_route": {
# #         "ipv6": {
# #             "count": {
# #                 "total-routes": "4"
# #             },
# #             "entry": [
# #                 {
# #                     "active": "Y",
# #                     "ipaddress": "2001:4888:26f:4100::/56",
# #                     "metric": "1",
# #                     "next-hop": {
# #                         "interface": "n/a",
# #                         "next-hop": "n/a"
# #                     },
# #                     "preference": "5",
# #                     "tag": "1000",
# #                     "type": "BH"
# #                 },
# #                 {
# #                     "active": "N",
# #                     "ipaddress": "2001:4888:26f:4140::/64",
# #                     "metric": "1",
# #                     "next-hop": {
# #                         "interface": "n/a",
# #                         "next-hop": "n/a"
# #                     },
# #                     "preference": "5",
# #                     "tag": "1000",
# #                     "type": "BH"
# #                 },
# #                 {
# #                     "active": "Y",
# #                     "ipaddress": "2001:4888:2000:0:645:2a0::/112",
# #                     "metric": "1",
# #                     "next-hop": {
# #                         "interface": "n/a",
# #                         "next-hop": "n/a"
# #                     },
# #                     "preference": "5",
# #                     "tag": "1000",
# #                     "type": "BH"
# #                 },
# #                 {
# #                     "active": "Y",
# #                     "ipaddress": "2001:4888:2062:3000::/52",
# #                     "metric": "1",
# #                     "next-hop": {
# #                         "interface": "n/a",
# #                         "next-hop": "n/a"
# #                     },
# #                     "preference": "5",
# #                     "tag": "1000",
# #                     "type": "BH"
# #                 }
# #             ]
# #         }
# #     }
# # }
# # ]"""
# #     assert result == ipv6_result


# # def test_show_router_route_table():
# #     """Test parsing show router route table."""
# #     # TODO: Convert to fixture
# #     example_output = "tests/show_output/show_router_route_table.txt"
# #     parser = SrosParser(example_output)
# #     result = parser.show_router_route_table()
# #     routes = """[
# # {
# #     "route-table": [
# #         {
# #             "ipv4": {
# #                 "count": {
# #                     "total-routes": "7"
# #                 },
# #                 "entry": [
# #                     {
# #                         "age": "09h15m13s",
# #                         "ipaddress": "10.115.30.0/24",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     },
# #                     {
# #                         "age": "09h15m13s",
# #                         "ipaddress": "10.115.43.0/24",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     },
# #                     {
# #                         "age": "09h15m13s",
# #                         "ipaddress": "10.115.56.0/24",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     },
# #                     {
# #                         "age": "09h15m14s",
# #                         "ipaddress": "10.115.56.0/32",
# #                         "next-hop": {
# #                             "metric": "0",
# #                             "next-hop": "system"
# #                         },
# #                         "pref": "0",
# #                         "protocol": "Local",
# #                         "type": "Local"
# #                     },
# #                     {
# #                         "age": "09h15m13s",
# #                         "ipaddress": "10.119.228.0/23",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     },
# #                     {
# #                         "age": "09h15m13s",
# #                         "ipaddress": "10.119.228.16/28",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     },
# #                     {
# #                         "age": "09h15m13s",
# #                         "ipaddress": "10.253.236.0/23",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     }
# #                 ]
# #             }
# #         },
# #         {
# #             "ipv6": {
# #                 "count": {
# #                     "total-routes": "4"
# #                 },
# #                 "entry": [
# #                     {
# #                         "age": "09h18m31s",
# #                         "ipaddress": "2001:4888:26f:3100::/56",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     },
# #                     {
# #                         "age": "09h18m31s",
# #                         "ipaddress": "2001:4888:2000:0:645:1a0::/112",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     },
# #                     {
# #                         "age": "09h18m32s",
# #                         "ipaddress": "2001:4888:2000:0:645:1a0::/128",
# #                         "next-hop": {
# #                             "metric": "0",
# #                             "next-hop": "system"
# #                         },
# #                         "pref": "0",
# #                         "protocol": "Local",
# #                         "type": "Local"
# #                     },
# #                     {
# #                         "age": "09h18m31s",
# #                         "ipaddress": "2001:4888:2062:2000::/52",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     }
# #                 ]
# #             }
# #         }
# #     ]
# # }
# # ]"""
# #     assert result == routes
