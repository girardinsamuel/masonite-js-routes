"""A MasoniteJSRoutesProvider Service Provider."""
from masonite.providers import Provider
from masonite.views import View

from ..commands import InstallCommand, GenerateCommand
from ..generator import RoutesGenerator


class JSRoutesProvider(Provider):
    """Provides Services To The Service Container."""

    def __init__(self, app):
        self.application = app

    def register(self):
        """Register objects into the Service Container."""
        self.application.bind("config.js_routes", "masonite.js_routes.config.js_routes")
        self.application.make("commands").add(InstallCommand(), GenerateCommand())

    def boot(self, view: View):
        """Boots services required by the container."""
        # self.publishes(
        #     {os.path.join(package_directory, "config.py"): "config/js_routes.py"}
        # )
        self._register_routes_helper(view)

    def _register_routes_helper(self, view):
        generator = RoutesGenerator()

        def js_routes_helper(group=None, nonce=""):
            return generator.generate(group, nonce)

        view.share({"routes": js_routes_helper})
