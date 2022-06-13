"""A WelcomeController Module."""

from masonite.views import View
from masonite.controllers import Controller


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        return view.render("base")

    def posts(self, view: View):
        return "posts"

    def create_post(self):
        return 201

    def show_post(self, view: View):
        return "show_post"

    def show_post_comments(self):
        return 200
