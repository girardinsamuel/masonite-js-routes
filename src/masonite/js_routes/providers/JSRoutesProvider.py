"""A MasoniteJSRoutesProvider Service Provider."""
from masonite.packages import PackageProvider

from ..commands import GenerateCommand
from ..generator import RoutesGenerator


class JSRoutesProvider(PackageProvider):
    """Provides Services To The Service Container."""

    def configure(self):
        """Register objects into the Service Container."""
        self.root("masonite/js_routes").name("js_routes").config(
            "config/js_routes.py", publish=True
        )
        self.application.make("commands").add(GenerateCommand())
        self.generator = RoutesGenerator()

    def boot(self):
        """Boots services required by the container."""
        self.application.make("view").share({"routes": self.generator.generate})
