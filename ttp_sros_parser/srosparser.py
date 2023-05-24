"""TTP SROS Parser."""
import datetime
import json
import logging
import os
from dataclasses import dataclass
from typing import Dict, List, Optional, no_type_check

from ttp import ttp

from ttp_sros_parser.helpers import check_file, globfindfile


@dataclass
class SrosParser:  # pylint: disable=R0904
    """SrosParser."""

    config_file: str
    now: datetime.datetime = datetime.datetime.now()
    date: str = now.strftime("%b-%d-%Y")
    templates_path: str = f"{os.path.dirname(os.path.realpath(__file__))}/templates"

    def __post_init__(self) -> None:
        """Init."""
        check_file(self.config_file)
        logging.info("Loading all templates from 'templates/admin_display_file'")
        self.templates = globfindfile(f"{self.templates_path}/admin_display_file/*.ttp")

    def _parse(self, template: str) -> Dict[str, str]:
        """General Parser Private Method."""
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        return json.loads(parser.result(format="json")[0])[0]

    def _get_all_templates(self) -> List[str]:
        """Find all templates and return a complete list."""
        templates = globfindfile(f"{self.templates_path}/admin_display_file/*.ttp")
        return templates

    def get_router_interfaces(self) -> Dict[str, str]:
        """Extract all router interfaces from the base routing context."""
        template = f"{self.templates_path}/admin_display_file/sros_router_interface.ttp"
        return self._parse(template)

    def get_system_interface(self) -> Dict[str, str]:
        """Extract the system interface out of the host."""
        template = f"{self.templates_path}/helpers/sros_system_interface.ttp"
        return self._parse(template)

    def get_system_configuration(self) -> Dict[str, str]:
        """Extract system configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_system_configuration.ttp"
        return self._parse(template)

    def get_system_begin(self) -> Dict[str, str]:
        """Extract system configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_system_begin.ttp"
        return self._parse(template)

    @no_type_check
    def get_system_hostname(self) -> str:
        """Extract system hostname."""
        template = f"{self.templates_path}/helpers/sros_system_hostname.ttp"
        hostname = self._parse(template)
        return hostname["system"]["hostname"]

    def get_system_cards(self) -> Dict[str, str]:
        """Extract system card information, including MDAs."""
        template = f"{self.templates_path}/admin_display_file/sros_system_cards.ttp"
        return self._parse(template)

    def get_system_ethcfm(self) -> Dict[str, str]:
        """Extract system eth cfm information."""
        template = f"{self.templates_path}/admin_display_file/sros_system_ethcfm.ttp"
        return self._parse(template)

    def get_system_profiles(self) -> Dict[str, str]:
        """Extract system profiles."""
        template = f"{self.templates_path}/admin_display_file/sros_system_profiles.ttp"
        return self._parse(template)

    def get_connectors(self) -> Dict[str, str]:
        """Extract connector configurations."""
        template = f"{self.templates_path}/admin_display_file/sros_connector_configuration.ttp"
        return self._parse(template)

    def get_lags(self) -> Dict[str, str]:
        """Extract lag configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_7750_lag.ttp"
        return self._parse(template)

    def get_system_maf(self) -> Dict[str, str]:
        """Extract system MAF IP Filters, IPv4/6."""
        template = f"{self.templates_path}/admin_display_file/sros_system_maf.ttp"
        return self._parse(template)

    @no_type_check
    def get_system_asn(self) -> str:
        """Extract system ASN."""
        template = f"{self.templates_path}/helpers/sros_system_asn.ttp"
        asn = self._parse(template)
        return asn["system"]["router"]["autonomous-system"]

    def get_custom_template(self, template_path: str) -> Dict[str, str]:
        """Use custom template by passing in the template file location path.

        Custom templates should be stored in 'templates/custom_templates'
        """
        logging.info("Loading custom template %s", template_path)
        return self._parse(template_path)

    def show_bof(self) -> Dict[str, str]:
        """Parse the 'show bof' cli output."""
        template = f"{self.templates_path}/show_commands/sros_show_bof_cli.ttp"
        return self._parse(template)

    def get_system_service_sdp(self) -> Dict[str, str]:
        """Extract System > Service SDP's from SROS."""
        template = f"{self.templates_path}/admin_display_file/sros_system_service_sdp.ttp"
        return self._parse(template)

    def show_router_interface(self) -> Dict[str, str]:
        """Parse show router interface command."""
        template = f"{self.templates_path}/show_commands/sros_show_router_interface.ttp"
        return self._parse(template)

    def show_router_route_table(self) -> Dict[str, str]:
        """Parse show router route table."""
        template = f"{self.templates_path}/show_commands/show_router_router_table_general.ttp"
        return self._parse(template)

    def get_router_static_routes(self) -> Dict[str, str]:
        """Extract Static Route Configuration (v4/v6)."""
        template = f"{self.templates_path}/admin_display_file/sros_router_static_routes.ttp"
        return self._parse(template)

    def get_mgmt_router_config(self) -> Dict[str, str]:
        """Extract Static Route Configuration (v4/v6)."""
        template = f"{self.templates_path}/admin_display_file/sros_mgmt_router_config.ttp"
        return self._parse(template)

    def get_lsps(self) -> Dict[str, str]:
        """Extract MPLS LSP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_7750_mpls_lsp.ttp"
        return self._parse(template)

    def get_ports(self) -> Dict[str, str]:
        """Extract Port Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_port_config.ttp"
        return self._parse(template)

    def get_cflowd(self) -> Dict[str, str]:
        """Extract Cflowd Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_cflowd_config.ttp"
        return self._parse(template)

    def get_python_declaration_configuration(self) -> Dict[str, str]:
        """Parse Python declaration Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_7750_python_declaration_configuration.ttp"
        return self._parse(template)

    def get_filter_log_configuration(self) -> Dict[str, str]:
        """Parse filter logConfiguration."""
        template = f"{self.templates_path}/admin_display_file/sros_filter_log_configuration.ttp"
        return self._parse(template)

    def get_filter_match_list_configuration(self) -> Dict[str, str]:
        """Parse filter logConfiguration."""
        template = f"{self.templates_path}/admin_display_file/sros_filter_match_list_configuration.ttp"
        return self._parse(template)

    def get_system_security_configuration(self) -> Dict[str, str]:
        """System Security logConfiguration."""
        template = f"{self.templates_path}/admin_display_file/sros_system_security_config.ttp"
        return self._parse(template)

    def get_qos_policy_configuration(self) -> Dict[str, str]:
        """QOS Policy Configuration ."""
        template = f"{self.templates_path}/admin_display_file/sros_qos_policy_config.ttp"
        return self._parse(template)

    def get_qos_policy_configuration1(self) -> Dict[str, str]:
        """QOS Policy Configuration 1."""
        template = f"{self.templates_path}/admin_display_file/sros_qos_policy_config1.ttp"
        return self._parse(template)

    def get_qos_policy_configuration2(self) -> Dict[str, str]:
        """QOS Policy Configuration 2."""
        template = f"{self.templates_path}/admin_display_file/sros_qos_policy_config2.ttp"
        return self._parse(template)

    def get_python_configuration(self) -> Dict[str, str]:
        """Python Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_7750_python_configuration.ttp"
        return self._parse(template)

    def get_isis_configuration(self) -> Dict[str, str]:
        """ISIS Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_isis_configuration.ttp"
        return self._parse(template)

    def get_subscriber_mgmt_configuration(self) -> Dict[str, str]:
        """Subscriber Management Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_subscriber_mgmt_configuration.ttp"
        return self._parse(template)

    def get_aaa_declarations_configuration(self) -> Dict[str, str]:
        """AAA Declarations Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_aaa_declaration_config.ttp"
        return self._parse(template)

    def get_multicast_path_management_policy_configuration(self) -> Dict[str, str]:
        """Multicast Path Management Policy Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_multicast_path_management_policy_config.ttp"
        return self._parse(template)

    def get_port_xc_configuration(self) -> Dict[str, str]:
        """Port XC Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_port_cross-connect_config.ttp"
        return self._parse(template)

    def get_redundancy_configuration(self) -> Dict[str, str]:
        """Redundancy Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_redundancy_config.ttp"
        return self._parse(template)

    def get_filter_configuration(self) -> Dict[str, str]:
        """Filter Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_filter_configuration.ttp"
        return self._parse(template)

    def get_vrrp_configuration(self) -> Dict[str, str]:
        """VRRP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_vrrp_config.ttp"
        return self._parse(template)

    def get_igmp_configuration(self) -> Dict[str, str]:
        """IGMP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_igmp_config.ttp"
        return self._parse(template)

    def get_l2tp_configuration(self) -> Dict[str, str]:
        """L2TP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_l2tp_config.ttp"
        return self._parse(template)

    def get_router_policy_configuration(self) -> Dict[str, str]:
        """Policy Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_router_policy_config.ttp"
        return self._parse(template)

    def get_router_bgp_configuration(self) -> Dict[str, str]:
        """BGP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_router_bgp_config.ttp"
        return self._parse(template)

    def get_subscriber_mgmt_ss_configuration(self) -> Dict[str, str]:
        """Subscriber Management Service Side Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_subscriber_mgmt_ss_config.ttp"
        return self._parse(template)

    def get_mirror_configuration(self) -> Dict[str, str]:
        """Mirror Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_mirror_config.ttp"
        return self._parse(template)

    def get_radius_configuration(self) -> Dict[str, str]:
        """RADIUS Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_radius_config.ttp"
        return self._parse(template)

    def get_dhcp_configuration(self) -> Dict[str, str]:
        """DHCP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_dhcp_config.ttp"
        return self._parse(template)

    def get_twamp_light_config(self) -> Dict[str, str]:
        """Mirror Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_twamp_light_config.ttp"
        return self._parse(template)

    def get_aaa_configuration(self) -> Dict[str, str]:
        """AAA Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_aaa_config.ttp"
        return self._parse(template)

    def get_pim_configuration(self) -> Dict[str, str]:
        """PIM Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_pim_config.ttp"
        return self._parse(template)

    def get_ldp_configuration(self) -> Dict[str, str]:
        """LDP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_ldp_config.ttp"
        return self._parse(template)

    def show_file_dir(self) -> Dict[str, str]:
        """Extract file dir contents."""
        template = f"{self.templates_path}/show_commands/sros_file_dir.ttp"
        return self._parse(template)

    def show_service_service_using(self) -> Dict[str, str]:
        """Parse Service Service Using."""
        template = f"{self.templates_path}/show_commands/sros_show_service_service_using.ttp"
        return self._parse(template)

    def get_log_configuration(self) -> Dict[str, str]:
        """Parse Log Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_log_configuration.ttp"
        return self._parse(template)

    def get_system_time_ntp_config(self) -> Dict[str, str]:
        """Parse NTP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_system_time_ntp.ttp"
        return self._parse(template)

    def show_router_static_route(self, protocol: Optional[str] = "ipv4") -> Dict[str, str]:
        """Parse show router static-route.

        Must pass in protocol version of either "ipv4" or "ipv6".
        """
        if not protocol or protocol.lower() == "ipv4":
            logging.info("Missing protocol for static-route parsing, defaulting to IPV4.")
            template = f"{self.templates_path}/show_commands/sros_show_router_static_route_ipv4.ttp"
        elif protocol.lower() == "ipv6":
            template = f"{self.templates_path}/show_commands/sros_show_router_static_route_ipv6.ttp"

        return self._parse(template)

    def get_full_config(self) -> Dict[str, str]:
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

        return self._parse(template=full_config_template)
