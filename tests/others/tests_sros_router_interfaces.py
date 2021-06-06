from ttp_templates import parse_output
import pprint

data = """
#--------------------------------------------------
echo "Router (Network Side) Configuration"
#--------------------------------------------------
    router Base
        interface "L3-NGM-IDN-0165"
            no shutdown
        exit
        interface "L3-OAM-eNodeB0215"
            enable-ingress-stats
            no shutdown
        exit
        interface "L3-OAM-eNodeB0905"
            no shutdown
        exit
        interface "system"
            address 10.115.56.217/32
            ipv6
                address 2001:4888:1069:1222:699:400:0:d7/128 
            exit
            no shutdown
        exit
        interface "to-BTS0420-7705-HUB-01-1"
            address 172.25.195.89/31
            description "DESCT-to-TEMQAZKWT1A-P-AL-0415-H1-1"
            ldp-sync-timer 45
            port 1/5/8:3215
            ipv6
                address 2001:1222:206a:21cd:699:400:0:1/64 
                bfd 500 receive 500 multiplier 3
            exit
            qos 20120
            bfd 500 receive 500 multiplier 3
            no shutdown
        exit
#--------------------------------------------------
echo "Static Route Configuration"
#--------------------------------------------------
"""

result = parse_output(
    data=data, platform="sros", command="admin display router interfaces"
)
pprint.pprint(result)
