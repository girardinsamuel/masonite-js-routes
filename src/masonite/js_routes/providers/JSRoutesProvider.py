"""A MasoniteJSRoutesProvider Service Provider."""
from masonite.providers import Provider

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
        self.generator = RoutesGenerator()

    def boot(self):
        """Boots services required by the container."""
        self.application.make("view").share({"routes": self.generator.generate})
