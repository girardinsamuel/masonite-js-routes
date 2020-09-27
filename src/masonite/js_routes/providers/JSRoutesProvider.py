"""A JSRoutesProvider Service Provider."""
import os
from masonite.provider import ServiceProvider
from masonite.view import View
from masonite.js_routes.commands.GenerateCommand import GenerateCommand
from masonite.js_routes.commands.InstallCommand import InstallCommand

from ..generator import RoutesGenerator


package_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class JSRoutesProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        self.app.bind("GenerateCommand", GenerateCommand())
        self.app.bind("InstallCommand", InstallCommand())

    def boot(self, view: View):
        """Boots services required by the container."""
        self.publishes(
            {os.path.join(package_directory, "config.py"): "config/js_routes.py"}
        )
        self._register_routes_helper(view)

    def _register_routes_helper(self, view):
        generator = RoutesGenerator()

        def js_routes_helper(group=None, nonce=""):
            return generator.generate(group, nonce)

        view.share({"routes": js_routes_helper})
