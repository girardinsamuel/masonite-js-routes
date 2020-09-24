from jinja2 import Markup
from .routes import Routes


class RoutesGenerator(object):

    generated = False

    def generate(self, group=None, nonce=""):
        payload = Routes(group).to_json()

        # if already generated, only hydrate Ziggy.namedRoutes variable client-side
        if self.generated:
            return self._generate_merge_js(payload, nonce)

        self.generated = True
        return self._generate_base_js(payload, nonce)

    def _get_nonce_snippet(self, nonce):
        return 'nonce="{0}"'.format(nonce) if nonce else ""

    def _generate_base_js(self, payload, nonce):
        nonce_snippet = self._get_nonce_snippet(nonce)
        return Markup(
            "<script type='text/javascript'{0}>var Ziggy = {1};</script>".format(
                nonce_snippet, payload
            )
        )

    def _generate_merge_js(self, payload, nonce):
        nonce_snippet = self._get_nonce_snippet(nonce)
        snippet = [
            "<script type='text/javascript'{0}>".format(nonce_snippet),
            "   let routes = {0};".format(payload),
            "   (function() {",
            "       for (let name in routes) {",
            "           Ziggy.namedRoutes[name] = routes[name];",
            "       }",
            "   })();",
            "</script>",
        ]
        return Markup("\n".join(snippet))
