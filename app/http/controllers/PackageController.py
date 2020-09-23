"""Masonite JS Routes Controller"""

from masonite.view import View
from masonite.request import Request
from app.User import User

class MasoniteJSRoutesController:
    """Base controller for the package
    """

    def show(self, view: View, request: Request):

        return 'Hello World'
