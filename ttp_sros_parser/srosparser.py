"""TTP SROS Parser."""
import logging
import json
import datetime
import os
from typing import Optional
from ttp import ttp
from .helpers import globfindfile, check_file


class SrosParser:  # pylint: disable=R0904
    """SrosParser."""

    x = datetime.datetime.now()
    date = x.strftime("%b-%d-%Y")

    # Establish the local install dir of templates for the SrosParser package.
    templates = f"{os.path.dirname(os.path.realpath(__file__))}/templates"

    def __init__(self, config_file):
        """Init."""
        self.config_file = check_file(config_file)
        self.templates_path = SrosParser.templates
        self.templates = globfindfile(f"{self.templates_path}/admin_display_file/*.ttp")
        logging.info("Loading all templates from 'templates/admin_display_file'")
        self.date = SrosParser.date

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

    def get_lsps(self, json_format: bool = True):
        """Extract MPLS LSP Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_7750_mpls_lsp.ttp"
        return self._parse(template, json_format=json_format)

    def get_ports(self, json_format: bool = True):
        """Extract Port Configuration."""
        template = f"{self.templates_path}/admin_display_file/sros_port_config.ttp"
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
