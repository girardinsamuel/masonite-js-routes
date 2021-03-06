import json
import re
from urllib.parse import urlsplit
from masonite.helpers import config
from masonite.helpers.routes import flatten_routes
from masonite import env
from .helpers import matches


def convert_uri(uri):
    """Convert routes defined as /users/@user to users/{user} so
    that Ziggy can process it client-side"""

    # it should handle optional parameters
    uri = uri.replace("?", "@")
    # remove typed param hint before further parsing
    for hint in [":int", ":string"]:
        if hint in uri:
            uri = uri.replace(hint, "")
    url = re.sub(r"(@[\w]*)", r"{\1}", uri).replace("@", "")
    # remove leading slash already added by ziggy-js
    if url.startswith("/"):
        url = url[1:]
    return url


class Routes(object):
    def __init__(self, group=None):
        self.base_domain = ""
        self.base_port = None
        self.base_protocol = "http"
        self.base_url = env("APP_URL")
        self.parse_base_url()

        self.group = group
        self.routes = self.get_named_routes()

    def _config(self, key, default=False):
        """Get configuration key of the package more easily"""
        return config("js_routes.filters.{0}".format(key), default)

    def parse_base_url(self):
        url_object = urlsplit(self.base_url)
        self.base_protocol = url_object.scheme
        domain_tokens = url_object.netloc.split(":")
        if len(domain_tokens) > 1:
            self.base_port = domain_tokens[1]
        self.base_domain = domain_tokens[0]

    def get_named_routes(self):
        """Get a list of the application's named routes, keyed by their names."""
        from wsgi import container

        web_routes = container.make("WebRoutes")
        routes = {}
        for route in flatten_routes(web_routes):
            if route.named_route:
                routes.update(
                    {
                        route.named_route: {
                            "uri": convert_uri(route.route_url),
                            "methods": route.method_type,
                        }
                    }
                )
                if route.required_domain:
                    routes[route.named_route].update({"domain": route.required_domain})
                if route.list_middleware:
                    routes[route.named_route].update(
                        {"middleware": route.list_middleware}
                    )

        return routes

    def apply_filters(self, group):
        if group:
            return self.filter_by_groups(group)

        # return unfiltered routes if user set both config options.
        if self._config("except") and self._config("only"):
            return self.routes

        if self._config("except"):
            return self.except_routes()

        if self._config("only"):
            return self.only_routes()

        return self.routes

    def except_routes(self):
        return self.filter_routes(self._config("except"), False)

    def only_routes(self):
        return self.filter_routes(self._config("only"))

    def filter_by_groups(self, group):
        """Filters routes by group"""
        groups = self._config("groups")
        if isinstance(group, list):
            filters = []
            for group_name in group:
                filters += groups.get(group_name, [])
            return self.filter_routes(filters)
        else:
            # @josephmancuso it should work config("js_routes.filters.groups.welcome")
            groups = self._config("groups")
            groups_filters = groups.get(group, [])
            if groups_filters:
                return self.filter_routes(groups_filters)
        return self.routes

    def filter_routes(self, filters, include=True):
        """Filter routes by name using the given patterns."""
        if not isinstance(filters, list):
            filters = [filters]

        def filter_func(route):
            for f in filters:
                if matches(f, route[0]):
                    return include
            return not include

        return dict(filter(filter_func, self.routes.items()))

    def to_dict(self):
        return {
            "url": self.base_url,
            "port": self.base_port,
            "defaults": {},
            "routes": self.apply_filters(self.group),
        }

    def to_json(self):
        """Convert this Routes instance to JSON."""
        return json.dumps(self.to_dict())
