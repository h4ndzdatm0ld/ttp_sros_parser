from ttp import ttp
import glob, sys, json, os, datetime, logging


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Creating directory. " + directory)


def globfindfile(regex):
    """This function will simply locate a file in the DIR by passing the regex value (ie:(*.log))
    The returned value by calling the function is the file. If the path is passed in, the full path is returned back -
    not just the filename.
    """
    try:
        files = []
        if len(glob.glob(regex)) == 0:
            sys.exit(f"No {regex} file found.")
        else:
            for file in glob.glob(regex):
                files.append(file)
        return files

    except Exception as e:
        print(f"Something went wrong, {e}")


class SrosParser:

    x = datetime.datetime.now()
    date = x.strftime("%b-%d-%Y")

    # Establish the local install dir of templates for the SrosParser package.
    templates = f"{os.path.dirname(os.path.realpath(__file__))}/templates"

    def __init__(self, config_file):
        self.config_file = config_file
        self.templates_path = SrosParser.templates
        self.templates = globfindfile(f"{self.templates_path}/admin_display_file/*.ttp")
        logging.info("Loading all templates from 'templates/admin_display_file'")
        self.date = SrosParser.date

    def get_all_templates(self):
        """ Find all templates and return a complete list """
        templates = globfindfile(f"{self.templates_path}/admin_display_file/*.ttp")
        return templates

    def get_router_interfaces(self):
        """Extract all router interfaces from the base routing context
        Results are returned in JSON"""

        template = f"{self.templates_path}/admin_display_file/sros_router_interface.ttp"
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]
        return results

    def get_system_interface(self):
        """Extract the system interface out of the host."""

        template = f"{self.templates_path}/helpers/sros_system_interface.ttp"
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]
        return results

    def get_system_configuration(self):
        """Extract system configuration"""

        template = (
            f"{self.templates_path}/admin_display_file/sros_system_configuration.ttp"
        )
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]
        return results

    def get_system_hostname(self):
        """Extract system hostname"""

        template = f"{self.templates_path}/helpers/sros_system_hostname.ttp"
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]

        # Load str to json object
        name = json.loads(results)
        # Drill down into list and the system dict. Return only hostname.
        return name[0]["system"]["hostname"]

    def get_system_cards(self):
        """Extract system card information, including MDAs"""

        template = f"{self.templates_path}/admin_display_file/sros_system_cards.ttp"
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]

        return results

    def get_system_ethcfm(self):
        """Extract system eth cfm information"""

        template = f"{self.templates_path}/admin_display_file/sros_system_ethcfm.ttp"
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]

        return results

    def get_system_profiles(self):
        """Extract system profiles"""

        template = f"{self.templates_path}/admin_display_file/sros_system_profiles.ttp"
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]

        return results

    def get_system_maf(self):
        """Extract system MAF IP Filters, IPv4/6."""

        template = f"{self.templates_path}/admin_display_file/sros_system_maf.ttp"
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]

        return results

    def get_system_asn(self):
        """Extract system ASN """

        template = f"{self.templates_path}/helpers/sros_system_asn.ttp"
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]

        asn = json.loads(results)
        return asn[0]["system"]["router"]["autonomous-system"]

    def get_custom_template(self, template_path):
        """Use custom template by passing in the template file location path.
        Custom templates should be stored in 'templates/custom_templates'"""

        logging.info(f"Loading custom template, {template_path}")
        template = template_path
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]

        return results

    def show_bof(self, file_path="file", ravs=False):

        """Parse the 'show bof' cli output. For now this must be in
        the same text as the full config file. Most likely, appended
        to the end of a file after running, 'admin display-config'
        """
        TODO: "Had to add a conditional to retry the parser. Sometimes returns as list and other as str..?"

        if file_path != "file":
            data = file_path
        else:
            data = self.config_file

        if ravs == True:
            template = f"{self.templates_path}/show_commands/sros_show_ravs_bof_cli.ttp"
        else:
            template = f"{self.templates_path}/show_commands/sros_show_bof_cli.ttp"

        parser = ttp(data, template=template)
        parser.parse()
        results = parser.result(format="json")[0]

        if type(results) == list:        
            results = parser.result(format="json")[0]
            return results
        else:
            return results


    def get_system_service_sdp(self, file_path="file"):

        """Extract System > Service SDP's from SROS"""

        template = (
            f"{self.templates_path}/admin_display_file/sros_system_service_sdp.ttp"
        )
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]

        return results

    def show_router_interface(self):

        """Parse show router interface command"""

        template = (
            f"{self.templates_path}/show_commands/sros_show_router_interface.ttp"
        )
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]

        return results

    def show_router_route_table(self):

        """Parse show router route table"""

        template = (
            f"{self.templates_path}/show_commands/sros_show_router_route_table.ttp"
        )
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]
        print(results)

        return results

    def get_router_static_routes(self, file_path="file"):

        """Extract Static Route Configuration (v4/v6)"""

        template = (
            f"{self.templates_path}/admin_display_file/sros_router_static_routes.ttp"
        )
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]

        return results

    def show_file_dir(self):

        """Extract file dir contents"""

        template = f"{self.templates_path}/show_commands/sros_file_dir.ttp"
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]

        return results

    def show_service_service_using(self):

        """Parse Service Service Using"""

        template = (
            f"{self.templates_path}/show_commands/sros_show_service_service_using.ttp"
        )
        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]

        return results

    def show_router_static_route(self, protocol="protocol"):

        """Parse show router static-route. Must pass in protocol version
        of either IPV4 or IPV6."""

        if protocol.upper() == "IPV4":
            template = f"{self.templates_path}/show_commands/sros_show_router_static_route_ipv4.ttp"
        elif protocol.upper() == "IPV6":
            template = f"{self.templates_path}/show_commands/sros_show_router_static_route_ipv6.ttp"
        elif protocol == "protocol":
            print("Please specify IPV4 or IPV6.")

        parser = ttp(data=self.config_file, template=template)
        parser.parse()
        results = parser.result(format="json")[0]

        return results

    def get_full_7705_config(self):
        """Recreate 'get_full_config', but round up new set of templates with filenames
        containing '7705', for example."""
        pass

    def get_full_config(self):
        """Compile all templates and return a fully parsed config in json.
        Loop through and open all templates and create 1 large ttp parsing
        template. Once compiled, apply compiled template and generate full config.
        We skipp multiple templates that are redundant. A log file is created
        to include a list of templates used to generate compiled template."""

        templates = globfindfile(f"{self.templates_path}/admin_display_file/*.ttp")

        sros_fullconfig = (
            f"{self.templates_path}/admin_display_file/sros_full_config_latest.ttp"
        )

        with open(sros_fullconfig, "w+") as all_templates:
            lst_temps = []
            for template in templates:
                if (
                    "system_interface" in template
                    or "hostname" in template
                    or "full_config" in template
                    or "custom" in template
                ):  # Redundant, skipping.
                    logging.info(f"Dropping Template.. {template}")
                    pass
                else:
                    lst_temps.append(template)
                    with open(template, "r") as file:
                        some_template = file.read()
                        all_templates.write(some_template)

            logging.info(f"Compiling List of Templates Used: {lst_temps}")

        logging.info("Extracting hostname from configuration for filename.")
        parser = ttp(
            data=self.config_file,
            template=f"{self.templates_path}/helpers/sros_system_hostname.ttp",
        )
        parser.parse()
        results = parser.result(format="json")[0]
        name = json.loads(results)
        hostname = name[0]["system"]["hostname"]
        logging.info(f"Extracted hostname: {hostname}")

        #TODO: "Make this a file that gets returned to the user to do as they please with it."

        folder = f"Parsed-Configs/{self.date.upper()}"
        createFolder(folder)
        file = f"{folder}/{hostname}.cfg"
        logging.info(f"Generated File: {file}")

        with open(file, "w+") as data:
            parser = ttp(data=self.config_file, template=sros_fullconfig)
            parser.parse()

            results = parser.result(format="json")[0]

            data.write(f"{results}\n")

        return file
