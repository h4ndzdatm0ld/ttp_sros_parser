from ttp_templates import parse_output
import pprint

data = """

# Generated MON NOV 02 20:33:16 2020 UTC

exit all
configure
#--------------------------------------------------
echo "System Configuration"
#--------------------------------------------------
    system
        name "EXAMPLEPHX-P-AL-7750-01"
        contact "Hugo Tinoco"
        location "Phoenix, AZ"
        rollback
            rollback-location "cf2:\Rollback"
        exit
        snmp
            streaming
                no shutdown
            exit
            packet-size 9216
        exit
        time
            ntp
                ntp-server
                server 8.8.8.8
                server 8.8.4.4
                no authentication-check
                no shutdown
            exit
            sntp
                shutdown
            exit
            zone MST 
        exit
        script-control
            script "EHS-Egress-FCS-Errors" owner "EHS"
                description "EHS FCS Errors - generate TS file"
                location "cf2:\EHS\EHS-Script-FCS-Errors_7750_1.txt"
                no shutdown
            exit
            script-policy "EHS-script-policy" owner "EHS"
                results "cf2:\EHS\EHS-FCS-Script-Results"
                script "EHS-Egress-FCS-Errors" owner "EHS"
                max-completed 255
                expire-time 7776000
                no shutdown
            exit
        exit
    exit
#--------------------------------------------------
"""

result = parse_output(
    data=data, platform="sros", command="admin display system configuration"
)
pprint.pprint(result)
