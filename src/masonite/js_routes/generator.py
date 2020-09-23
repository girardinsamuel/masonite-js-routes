from jinja2 import Markup
from .routes import Routes


class RoutesGenerator(object):

    generated = False

    def generate(self, group=False, nonce=False):
        payload = Routes(group).to_json()
        nonce = ''

        if self.generated:
            return self.generate_merge_js(payload, nonce)

        self.generated = True

        return Markup("<script type='text/javascript'{nonce}>var Ziggy = {payload};</script>".format(nonce, payload))

    def generate_merge_js(json, nonce):
        return Markup("<script type='text/javascript'{nonce}>var routes = {json}; for (let name in routes) {\n  Ziggy.namedRoutes[name] = routes[name];\n  }\n})();</script>".format(nonce, json))

