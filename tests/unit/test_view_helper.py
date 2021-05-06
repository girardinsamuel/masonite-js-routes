from masonite.tests import TestCase
from masonite.routes import Route
from jinja2 import Markup

from src.masonite.js_routes.generator import RoutesGenerator


all_expected_routes = {
    "home": {"uri": "/home", "methods": ["GET"]},
    "posts.show": {"uri": "/posts/{post}", "methods": ["GET"]},
    "posts.store": {"uri": "/posts", "methods": ["POST"]},
    "posts.index": {"uri": "/posts", "methods": ["GET"]},
    "postComments.index": {"uri": "/posts/{post}/comments", "methods": ["GET"]},
    "postComments.show": {
        "uri": "/posts/{post}/comments/{comment}",
        "methods": ["GET"],
    },
    "admin.users.index": {"uri": "/admin/users", "methods": ["GET"]},
}


class TestViewHelper(TestCase):
    sqlite = False

    def setUp(self):
        super().setUp()
        self.setRoutes(
            Route.get("home", "TestController@show").name("home"),
            Route.get("posts", "TestController@show").name("posts.index"),
            Route.get("posts/@post", "TestController@show").name("posts.show"),
            Route.get("posts/@post/comments", "TestController@show").name("postComments.index"),
            Route.get("posts/@post/comments/@comment:int", "TestController@show").name(
                "postComments.show"
            ),
            Route.post("posts", "TestController@show").name("posts.store"),
            Route.get("admin/users", "TestController@show").name("admin.users.index"),
        )

    def test_generator_without_filters(self):
        generator = RoutesGenerator()
        markup = generator.generate()
        self.assertIsInstance(markup, Markup)

    # def test_generate_with_filter(self):
    #     from config.js_routes import FILTERS
    #     FILTERS["only"] = ["home"]
    #     generator = RoutesGenerator()
    #     markup = generator.generate()
