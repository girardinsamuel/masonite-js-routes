"""A InstallCommand Command."""
import os
from cleo import Command


package_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class InstallCommand(Command):
    """
    Publish js_routes config file.

    js_routes:install
    """

    def handle(self):
        # publish config files
        # create_or_append_config(os.path.join(package_directory, "config/js_routes.py"))
        self.info(
            "masonite-js-routes config file has been published to config/js_routes.py."
        )
