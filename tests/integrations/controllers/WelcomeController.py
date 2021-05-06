"""A WelcomeController Module."""

from masonite.views import View
from masonite.controllers import Controller


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        return view.render("base")

    def posts(self, view: View):
        return "posts"

    def show_post(self, view: View):
        return "show_post"
