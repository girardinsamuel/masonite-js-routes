import json
from urllib.parse import urlsplit
from masonite.helpers import config
from masonite.helpers.routes import flatten_routes


class Routes(object):

    def __init__(self, group="", url=""):
        self.base_domain = ""
        self.base_port = None
        self.base_protocol = "http"
        self.base_url = url + "/" if not url.endswith("/") else url
        self.parse_base_url()

        self.group = group
        self.routes = self.get_named_routes()

    def _config(self, key):
        """Get configuration key of the package more easily"""
        return config("js_routes.{0}".format(key))

    def parse_base_url(self):
        url_object = urlsplit(self.base_url)
        self.base_protocol = url_object.scheme
        self.base_domain, self.base_port = url_object.netloc.split(":")

    def get_named_routes(self):
        """Get a list of the application's named routes, keyed by their names."""
        from routes.web import ROUTES
        routes = []
        for route in flatten_routes(ROUTES):
            if route.named_route:
                routes.update({route.named_route: {"uri": route.route_url, "methods": []})
                if self.is_in(route.named_route, "except"):
                    self.append_route_to_list(route.named_route, "except")
                elif self.is_in(route.named_route, "only"):
                    self.append_route_to_list(route.named_route, "only")

                # get routes methods and add other info if required
        return self.routes

    def is_in(self, route_name, filter_list):
        return route_name in self._config(filter_list, [])

    def apply_filters(self, group):
        if (group):
            return self.group(group)

        # return unfiltered routes if user set both config options.
        if self._config('except') and self._config('only'):
            return self.routes

        if self._config('except'):
            return self.except_routes()

        if self._config('only'):
            return self.only_routes()

    def except_routes(self):
        return self.filter(self._config("except", False))

    def only_routes(self):
        return self.filter(self._config("only"), False)

    def group(self, group):
        """Filters routes by group"""

        if isinstance(group, dict):
            filters = []
            for group_name, group_filters in self._config("groups"):
                # filters = { **group_filters, **filters }
                filters += group_filters
                return self.filter(filters)

        if self._config("groups.{0}".format(group)):
            return self.filter(self._config("groups.{0}".format(group)))

    def filter(self, filters, include=True):
        """Filter routes by name using the given patterns."""
        # TODO
        return self.routes

    def to_dict(self):
        return {
            "baseUrl": self.base_url,
            "baseProtocol": self.base_protocol,
            "baseDomain": self.base_domain,
            "basePort": self.base_port,
            "defaultParameters": [],  # TODO ?
            "namedRoutes": self.apply_filters(self.group)
        }

    def to_json(self):
        """Convert this Routes instance to JSON."""
        return json.dump(self.to_dict())


def append_route_to_list(route, list):
    """Append route to list in package configuration."""
    # TODO
    pass

