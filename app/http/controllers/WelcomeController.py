"""Masonite JS Routes Controller"""
from masonite.view import View
from masonite.request import Request
from masonite.controllers import Controller


class WelcomeController(Controller):
    """Base controller for the package
    """
    def __init__(self, request: Request):
        """WelcomeController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render("welcome")

    def user(self, view: View):
        return view.render("user", {"user": self.request.param("user")})

    def user_with_check(self, view: View):
        return view.render("user", {"user": self.request.param("user")})

    def user_or_anonymous(self, view: View):
        user = self.request.param("user") or "Anonymous"
        return view.render("user", {"user": user })

    def two_users(self, view: View):
        return view.render("user", {"user1": self.request.param("user1"),
                                    "user2": self.request.param("user2")})
