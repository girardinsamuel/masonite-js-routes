from masonite.testing import TestCase
from masonite.routes import Get, Post
from src.masonite.js_routes.routes import Routes as JsRoutes


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


class TestRoutes(TestCase):
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

    def test_basic_routes_generation(self):
        js_routes = JsRoutes()
        routes = js_routes.routes
        self.assertEqual(all_expected_routes, routes)

    def test_can_filter_to_only_include_routes_matching_a_pattern(self):
        js_routes = JsRoutes()
        routes = js_routes.filter_routes(["posts.s*", "home"])
        expected = {
            "home": {"uri": "/home", "methods": ["GET"]},
            "posts.show": {"uri": "/posts/{post}", "methods": ["GET"]},
            "posts.store": {"uri": "/posts", "methods": ["POST"]},
        }
        self.assertEqual(expected, routes)

    def test_can_filter_to_exclude_routes_matching_a_pattern(self):
        js_routes = JsRoutes()
        routes = js_routes.filter_routes(["posts.s*", "home", "admin.*"], False)
        expected = {
            "posts.index": {"uri": "/posts", "methods": ["GET"]},
            "postComments.index": {"uri": "/posts/{post}/comments", "methods": ["GET"]},
            "postComments.show": {
                "uri": "/posts/{post}/comments/{comment}",
                "methods": ["GET"],
            },
        }

        self.assertEqual(expected, routes)

    def test_can_set_included_routes_using_only_config(self):
        from config.js_routes import FILTERS

        FILTERS["except"] = []
        FILTERS["only"] = ["posts.s*", "home"]
        routes = JsRoutes().to_dict()["namedRoutes"]
        expected = {
            "home": {"uri": "/home", "methods": ["GET"]},
            "posts.show": {"uri": "/posts/{post}", "methods": ["GET"]},
            "posts.store": {"uri": "/posts", "methods": ["POST"]},
        }
        self.assertEqual(expected, routes)

    def test_can_set_included_routes_using_except_config(self):
        from config.js_routes import FILTERS

        FILTERS["only"] = []
        FILTERS["except"] = ["posts.s*", "home"]
        routes = JsRoutes().to_dict()["namedRoutes"]
        expected = {
            "posts.index": {"uri": "/posts", "methods": ["GET"]},
            "postComments.index": {"uri": "/posts/{post}/comments", "methods": ["GET"]},
            "postComments.show": {
                "uri": "/posts/{post}/comments/{comment}",
                "methods": ["GET"],
            },
            "admin.users.index": {"uri": "/admin/users", "methods": ["GET"]},
        }
        self.assertEqual(expected, routes)

    def test_returns_unfiltered_routes_when_both_only_and_except_configs_set(self):
        from config.js_routes import FILTERS

        FILTERS["except"] = ["posts.s*", "home"]
        FILTERS["only"] = ["some.other.routes"]

        routes = JsRoutes().to_dict()["namedRoutes"]
        self.assertEqual(all_expected_routes, routes)

    def test_can_set_included_routes_using_groups_config(self):
        from config.js_routes import FILTERS

        FILTERS["groups"] = {"posts": ["posts.s*"]}
        routes = JsRoutes("posts").to_dict()["namedRoutes"]
        expected = {
            "posts.show": {"uri": "/posts/{post}", "methods": ["GET"]},
            "posts.store": {"uri": "/posts", "methods": ["POST"]},
        }
        self.assertEqual(expected, routes)

    def test_can_set_included_routes_using_groups_array_config(self):
        from config.js_routes import FILTERS

        FILTERS["groups"] = {"posts": ["posts.s*"], "admin": ["admin.*"]}
        routes = JsRoutes(["posts", "admin"]).to_dict()["namedRoutes"]
        expected = {
            "posts.show": {"uri": "/posts/{post}", "methods": ["GET"]},
            "posts.store": {"uri": "/posts", "methods": ["POST"]},
            "admin.users.index": {"uri": "/admin/users", "methods": ["GET"]},
        }
        self.assertEqual(expected, routes)

    def can_ignore_passed_group_not_set_in_config(self):
        from config.js_routes import FILTERS

        FILTERS["groups"] = {"posts": ["posts.s*"]}
        routes = JsRoutes(["unknown_group"]).to_dict()["namedRoutes"]
        self.assertEqual(all_expected_routes, routes)

    def can_include_middleware(self):
        pass

    def can_include_only_middleware_set_in_config(self):
        pass
