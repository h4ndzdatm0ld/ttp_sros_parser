from ttp_templates import parse_output
import pprint

data = """
*A:TEMPE-AZ-HUB-EXAMPLE-7750-01>config>service>ies>if>ipv6>vrrp# show router interface 

===============================================================================
Interface Table (Router: Base)
===============================================================================
Interface-Name                   Adm       Opr(v4/v6)  Mode    Port/SapId
   IP-Address                                                  PfxState
-------------------------------------------------------------------------------
L3-TELCO-IXR01-1               Up        Down/Down   IES     lag-1:300
   2001:1000:2062:357a:646:100:0:1/64                          INACCESSIBLE
   2001:1666:2062:357a:646:100:0:1/64                          INACCESSIBLE
   fe80::645:100:0:1/64                                        INACCESSIBLE
L3-TELCO-IXR02-1               Up        Down/Up     IES     lag-2:300
   2001:1666:2062:4222:649:100:0:1/64                          PREFERRED
   fe80::645:100:0:1/64                                        PREFERRED
L3-TELCO-eNodeB0420-DUL-01     Up        Up/Up       IES     1/1/c2/1:301
   10.0.0.0/31                                                 n/a
   2001:1000:2062:24ae:649:100::/64                            PREFERRED
   fe80::c8:ffff:fe00:0/64                                     PREFERRED
system                           Up        Up/Up       Network system
   10.100.43.69/32                                             n/a
   2001:4777:2062:2000:645:100:0:19f/128                       PREFERRED
to-7750-01                       Up        Up/Up       Network 1/1/c4/1:3415
   172.20.200.69/31                                           n/a
   2001:1666:206a:335d:645:100:0:1/64                          PREFERRED
   fe80::c8:ffff:fe00:0/64                                     PREFERRED
to-BTS0420-7750-H2               Up        Down/Down   Network lag-11:4094
   172.20.200.1/31                                           n/a
   2001:1666:206a:335f:645:100::/64                            INACCESSIBLE
   fe80::c8:ffff:fe00:14b/64                                   INACCESSIBLE
-------------------------------------------------------------------------------
Interfaces : 6
===============================================================================
"""

result = parse_output(data=data, platform="sros", command="show_router_interface")
pprint.pprint(result)
