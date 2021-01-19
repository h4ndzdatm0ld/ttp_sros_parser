How to setup tests by importing ttp_templates:

- Create the template following the guidelines which mimic the NTC Templates testing.
for example, for the sros devices:

result = parse_output(
    data=data,
    platform="sros",
    command="admin display router interfaces"
)

The templates must exist and follow the platform naming 'sros_admin_display_router_interfaces.txt'
and be put into the ttp_template folder after doing a pip3 install ttp_templats