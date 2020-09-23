"""A JsRoutesProvider Service Provider."""

from masonite.provider import ServiceProvider
from masonite.view import View

from masonite.js_routes.generator import RoutesGenerator


class JsRoutesProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        pass

    def boot(self, view: View):
        """Boots services required by the container."""
        self._register_routes_helper(view)

    def _register_routes_helper(self, view):
        generator = RoutesGenerator()

        def routes_helper(group):
            return generator.generate(group)

        view.share({
            "routes": routes_helper
        })
