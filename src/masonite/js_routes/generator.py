from jinja2 import Markup
from .routes import Routes


class RoutesGenerator:
    def generate(self, group=None, nonce=""):
        payload = Routes(group).to_json()
        return self._generate_base_js(payload, nonce)

    def generate_for_file(self, group=None):
        """Generate method used by command to generate directly a javascript
        file."""
        payload = Routes(group).to_json()
        content = "var Ziggy = {0};".format(payload) + "\n\nexport { Ziggy };"
        return content

    def _get_nonce_snippet(self, nonce):
        return 'nonce="{0}"'.format(nonce) if nonce else ""

    def _generate_base_js(self, payload, nonce):
        nonce_snippet = self._get_nonce_snippet(nonce)
        return Markup(
            "<script type='text/javascript'{0}>var Ziggy = {1};</script>".format(
                nonce_snippet, payload
            )
        )
