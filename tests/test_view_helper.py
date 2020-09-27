from masonite.testing import TestCase
from masonite.routes import Get, Post
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
    def setUp(self):
        super().setUp()
        self.routes(
            only=[
                Get("home", "tests.TestController@show").name("home"),
                Get("posts", "tests.TestController@show").name("posts.index"),
                Get("posts/@post", "tests.TestController@show").name("posts.show"),
                Get("posts/@post/comments", "tests.TestController@show").name(
                    "postComments.index"
                ),
                Get(
                    "posts/@post/comments/@comment:int", "tests.TestController@show"
                ).name("postComments.show"),
                Post("posts", "tests.TestController@show").name("posts.store"),
                Get("admin/users", "tests.TestController@show").name(
                    "admin.users.index"
                ),
            ]
        )
        self.buildOwnContainer()

    def test_generator_without_filters(self):
        generator = RoutesGenerator()
        markup = generator.generate()
        self.assertIsInstance(markup, Markup)

    # def test_generate_with_filter(self):
    #     from config.js_routes import FILTERS
    #     FILTERS["only"] = ["home"]
    #     generator = RoutesGenerator()
    #     markup = generator.generate()
    #     import pdb
    #     pdb.set_trace()
    #     self.assertEqual("<script type=\"text/javascript\">var Ziggy = {'baseUrl': '/', 'baseProtocol': '', 'baseDomain': '', 'basePort': null, 'defaultParameters': [], 'namedRoutes': {'home': {'uri': '/home', 'methods': ['GET']}}};</script>",
    #                      str(markup))
