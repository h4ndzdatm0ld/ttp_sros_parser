"""TTP SROS Parser."""
import datetime
import json
import logging
import os
from dataclasses import dataclass
from typing import Optional

from ttp import ttp

from .helpers import check_file, globfindfile


@dataclass
class SrosParser:  # pylint: disable=R0904
    """SrosParser."""

    x = datetime.datetime.now()
    date = x.strftime("%b-%d-%Y")
    templates_path = f"{os.path.dirname(os.path.realpath(__file__))}/templates"
    config_file: str

    def __post_init__(self):
        """Init."""
        check_file(self.config_file)
        logging.info("Loading all templates from 'templates/admin_display_file'")
        self.templates = globfindfile(f"{self.templates_path}/admin_display_file/*.ttp")

    def _parse(self, template: str, json_format=True):
        """General Parser Private Method."""
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]

        if json_format:
            results = json.loads(results)
        return results

    def _get_all_templates(self):
        """Find all templates and return a complete list."""
        templates = globfindfile(f"{self.templates_path}/admin_display_file/*.ttp")
        return templates

    def get_router_interfaces(self, json_format: bool = True):
        """Extract all router interfaces from the base routing context."""
        template = f"{self.templates_path}/admin_display_file/sros_router_interface.ttp"
        return self._parse(template, json_format=json_format)

    def get_system_interface(self, json_format: bool = True):
        """Extract the system interface out of the host."""
        template = f"{self.templates_path}/helpers/sros_system_interface.ttp"
        return self._parse(template, json_format=json_format)

    def get_system_configuration(self, json_format: bool = True):
        """Extract system configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_system_configuration.ttp"
        return self._parse(template, json_format=json_format)

    def get_system_begin(self, json_format: bool = True):
        """Extract system configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_system_begin.ttp"
        return self._parse(template, json_format=json_format)

    def get_system_hostname(self, json_format: bool = True):
        """Extract system hostname."""
        template = f"{self.templates_path}/helpers/sros_system_hostname.ttp"
        hostname = self._parse(template, json_format=json_format)
        return hostname[0]["system"]["hostname"]

    def get_system_cards(self, json_format: bool = True):
        """Extract system card information, including MDAs."""
        template = f"{self.templates_path}/admin_display_file/sros_system_cards.ttp"
        return self._parse(template, json_format=json_format)

    def get_system_ethcfm(self, json_format: bool = True):
        """Extract system eth cfm information."""
        template = f"{self.templates_path}/admin_display_file/sros_system_ethcfm.ttp"
        return self._parse(template, json_format=json_format)

    def get_system_profiles(self, json_format: bool = True):
        """Extract system profiles."""
        template = f"{self.templates_path}/admin_display_file/sros_system_profiles.ttp"
        return self._parse(template, json_format=json_format)

    def get_connectors(self, json_format: bool = True):
        """Extract connector configurations."""
        template = f"{self.templates_path}/admin_display_file/sros_connector_configuration.ttp"
        return self._parse(template, json_format=json_format)

    def get_lags(self, json_format: bool = True):
        """Extract lag configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_7750_lag.ttp"
        return self._parse(template, json_format=json_format)

    def get_system_maf(self, json_format: bool = True):
        """Extract system MAF IP Filters, IPv4/6."""
        template = f"{self.templates_path}/admin_display_file/sros_system_maf.ttp"
        return self._parse(template, json_format=json_format)

    def get_system_asn(self):
        """Extract system ASN."""
        template = f"{self.templates_path}/helpers/sros_system_asn.ttp"
        asn = self._parse(template, json_format=True)
        return asn[0]["system"]["router"]["autonomous-system"]

    def get_custom_template(self, template_path, json_format: bool = True):
        """Use custom template by passing in the template file location path.

        Custom templates should be stored in 'templates/custom_templates'
        """
        logging.info("Loading custom template %s", template_path)
        return self._parse(template_path, json_format=json_format)

    def show_bof(self):
        """Parse the 'show bof' cli output."""
        template = f"{self.templates_path}/show_commands/sros_show_bof_cli.ttp"
        return self._parse(template)

    def get_system_service_sdp(self, json_format: bool = True):
        """Extract System > Service SDP's from SROS."""
        template = f"{self.templates_path}/admin_display_file/sros_system_service_sdp.ttp"
        return self._parse(template, json_format=json_format)

    def show_router_interface(self, json_format: bool = True):
        """Parse show router interface command."""
        template = f"{self.templates_path}/show_commands/sros_show_router_interface.ttp"
        return self._parse(template, json_format=json_format)

    def show_router_route_table(self, json_format: bool = True):
        """Parse show router route table."""
        template = f"{self.templates_path}/show_commands/show_router_router_table_general.ttp"
        return self._parse(template, json_format=json_format)

    def get_router_static_routes(self, json_format: bool = True):
        """Extract Static Route Configuration (v4/v6)."""
        template = f"{self.templates_path}/admin_display_file/sros_router_static_routes.ttp"
        return self._parse(template, json_format=json_format)

    def get_mgmt_router_config(self, json_format: bool = True):
        """Extract Static Route Configuration (v4/v6)."""
        template = f"{self.templates_path}/admin_display_file/sros_mgmt_router_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_lsps(self, json_format: bool = True):
        """Extract MPLS LSP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_7750_mpls_lsp.ttp"
        return self._parse(template, json_format=json_format)

    def get_ports(self, json_format: bool = True):
        """Extract Port Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_port_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_cflowd(self, json_format: bool = True):
        """Extract Cflowd Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_cflowd_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_python_declaration_configuration(self, json_format: bool = True):
        """Parse Python declaration Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_7750_python_declaration_configuration.ttp"
        return self._parse(template, json_format=json_format)

    def get_filter_log_configuration(self, json_format: bool = True):
        """Parse filter logConfiguration."""
        template = f"{self.templates_path}/admin_display_file/sros_filter_log_configuration.ttp"
        return self._parse(template, json_format=json_format)

    def get_filter_match_list_configuration(self, json_format: bool = True):
        """Parse filter logConfiguration."""
        template = f"{self.templates_path}/admin_display_file/sros_filter_match_list_configuration.ttp"
        return self._parse(template, json_format=json_format)

    def get_system_security_configuration(self, json_format: bool = True):
        """System Security logConfiguration."""
        template = f"{self.templates_path}/admin_display_file/sros_system_security_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_qos_policy_configuration(self, json_format: bool = True):
        """QOS Policy Configuration ."""
        template = f"{self.templates_path}/admin_display_file/sros_qos_policy_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_qos_policy_configuration1(self, json_format: bool = True):
        """QOS Policy Configuration 1."""
        template = f"{self.templates_path}/admin_display_file/sros_qos_policy_config1.ttp"
        return self._parse(template, json_format=json_format)

    def get_qos_policy_configuration2(self, json_format: bool = True):
        """QOS Policy Configuration 2."""
        template = f"{self.templates_path}/admin_display_file/sros_qos_policy_config2.ttp"
        return self._parse(template, json_format=json_format)

    def get_python_configuration(self, json_format: bool = True):
        """Python Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_7750_python_configuration.ttp"
        return self._parse(template, json_format=json_format)

    def get_isis_configuration(self, json_format: bool = True):
        """ISIS Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_isis_configuration.ttp"
        return self._parse(template, json_format=json_format)

    def get_subscriber_mgmt_configuration(self, json_format: bool = True):
        """Subscriber Management Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_subscriber_mgmt_configuration.ttp"
        return self._parse(template, json_format=json_format)

    def get_aaa_declarations_configuration(self, json_format: bool = True):
        """AAA Declarations Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_aaa_declaration_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_multicast_path_management_policy_configuration(self, json_format: bool = True):
        """Multicast Path Management Policy Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_multicast_path_management_policy_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_port_xc_configuration(self, json_format: bool = True):
        """Port XC Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_port_cross-connect_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_redundancy_configuration(self, json_format: bool = True):
        """Redundancy Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_redundancy_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_filter_configuration(self, json_format: bool = True):
        """Filter Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_filter_configuration.ttp"
        return self._parse(template, json_format=json_format)

    def get_vrrp_configuration(self, json_format: bool = True):
        """VRRP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_vrrp_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_igmp_configuration(self, json_format: bool = True):
        """IGMP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_igmp_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_l2tp_configuration(self, json_format: bool = True):
        """L2TP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_l2tp_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_router_policy_configuration(self, json_format: bool = True):
        """Policy Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_router_policy_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_router_bgp_configuration(self, json_format: bool = True):
        """BGP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_router_bgp_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_subscriber_mgmt_ss_configuration(self, json_format: bool = True):
        """Subscriber Management Service Side Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_subscriber_mgmt_ss_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_mirror_configuration(self, json_format: bool = True):
        """Mirror Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_mirror_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_radius_configuration(self, json_format: bool = True):
        """RADIUS Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_radius_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_dhcp_configuration(self, json_format: bool = True):
        """DHCP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_dhcp_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_twamp_light_config(self, json_format: bool = True):
        """Mirror Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_twamp_light_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_aaa_configuration(self, json_format: bool = True):
        """AAA Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_aaa_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_pim_configuration(self, json_format: bool = True):
        """PIM Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_pim_config.ttp"
        return self._parse(template, json_format=json_format)

    def get_ldp_configuration(self, json_format: bool = True):
        """LDP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_ldp_config.ttp"
        return self._parse(template, json_format=json_format)

    def show_file_dir(self, json_format: bool = True):
        """Extract file dir contents."""
        template = f"{self.templates_path}/show_commands/sros_file_dir.ttp"
        return self._parse(template, json_format=json_format)

    def show_service_service_using(self, json_format: bool = True):
        """Parse Service Service Using."""
        template = f"{self.templates_path}/show_commands/sros_show_service_service_using.ttp"
        return self._parse(template, json_format=json_format)

    def get_log_configuration(self, json_format: bool = True):
        """Parse Log Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_log_configuration.ttp"
        return self._parse(template, json_format=json_format)

    def get_system_time_ntp_config(self, json_format: bool = True):
        """Parse NTP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_system_time_ntp.ttp"
        return self._parse(template, json_format=json_format)

    def show_router_static_route(self, protocol: Optional[str] = "ipv4"):
        """Parse show router static-route.

        Must pass in protocol version of either "ipv4" or "ipv6".
        """
        if not protocol or protocol.lower() == "ipv4":
            logging.info("Missing protocol for static-route parsing, defaulting to IPV4.")
            template = f"{self.templates_path}/show_commands/sros_show_router_static_route_ipv4.ttp"
        elif protocol.lower() == "ipv6":
            template = f"{self.templates_path}/show_commands/sros_show_router_static_route_ipv6.ttp"

        return self._parse(template)

    def get_full_config(self, json_format: bool = True):
        """Compile all templates and return a fully parsed config in json.

        Loop through and open all templates and create 1 large ttp parsing
        template. Once compiled, apply compiled template and generate full config.
        """
        templates = globfindfile(f"{self.templates_path}/admin_display_file/*.ttp")
        full_config_template = f"{self.templates_path}/full_config/sros_full_config.ttp"

        with open(full_config_template, "w+", encoding="utf-8") as full_config:
            for template in templates:
                with open(template, "r", encoding="utf-8") as file:
                    full_config.write(file.read())

        return self._parse(template=full_config_template, json_format=json_format)
