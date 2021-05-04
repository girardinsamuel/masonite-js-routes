from masonite.tests import TestCase
from masonite.routes import Route

from src.masonite.js_routes.routes import Routes as JsRoutes
from src.masonite.js_routes.config.js_routes import FILTERS

all_expected_routes = {
    "home": {"uri": "home", "methods": ["GET"]},
    "posts.show": {"uri": "posts/{post}", "methods": ["GET"]},
    "posts.store": {"uri": "posts", "methods": ["POST"]},
    "posts.index": {"uri": "posts", "methods": ["GET"]},
    "postComments.index": {"uri": "posts/{post}/comments", "methods": ["GET"]},
    "postComments.show": {
        "uri": "posts/{post}/comments/{comment}",
        "methods": ["GET"],
    },
    "admin.users.index": {"uri": "admin/users", "methods": ["GET"]},
}


class TestRoutes(TestCase):
    def setUp(self):
        super().setUp()
        self.setRoutes(
            Route.get("home", "TestController@show").name("home"),
            Route.get("posts", "TestController@show").name("posts.index"),
            Route.get("posts/@post", "TestController@show").name("posts.show"),
            Route.get("posts/@post/comments", "TestController@show").name(
                "postComments.index"
            ),
            Route.get("posts/@post/comments/@comment:int", "TestController@show").name(
                "postComments.show"
            ),
            Route.post("posts", "TestController@show").name("posts.store"),
            Route.get("admin/users", "TestController@show").name("admin.users.index"),
        )

    def test_basic_routes_generation(self):
        js_routes = JsRoutes()
        routes = js_routes.routes
        self.assertEqual(all_expected_routes, routes)

    def test_can_filter_to_only_include_routes_matching_a_pattern(self):
        js_routes = JsRoutes()
        routes = js_routes.filter_routes(["posts.s*", "home"])
        expected = {
            "home": {"uri": "home", "methods": ["GET"]},
            "posts.show": {"uri": "posts/{post}", "methods": ["GET"]},
            "posts.store": {"uri": "posts", "methods": ["POST"]},
        }
        self.assertEqual(expected, routes)

    def test_can_filter_to_exclude_routes_matching_a_pattern(self):
        js_routes = JsRoutes()
        routes = js_routes.filter_routes(["posts.s*", "home", "admin.*"], False)
        expected = {
            "posts.index": {"uri": "posts", "methods": ["GET"]},
            "postComments.index": {"uri": "posts/{post}/comments", "methods": ["GET"]},
            "postComments.show": {
                "uri": "posts/{post}/comments/{comment}",
                "methods": ["GET"],
            },
        }

        self.assertEqual(expected, routes)

    def test_can_set_included_routes_using_only_config(self):
        FILTERS["except"] = []
        FILTERS["only"] = ["posts.s*", "home"]
        routes = JsRoutes().to_dict()["routes"]
        expected = {
            "home": {"uri": "home", "methods": ["GET"]},
            "posts.show": {"uri": "posts/{post}", "methods": ["GET"]},
            "posts.store": {"uri": "posts", "methods": ["POST"]},
        }
        self.assertEqual(expected, routes)

    def test_can_set_included_routes_using_except_config(self):
        FILTERS["only"] = []
        FILTERS["except"] = ["posts.s*", "home"]
        routes = JsRoutes().to_dict()["routes"]
        expected = {
            "posts.index": {"uri": "posts", "methods": ["GET"]},
            "postComments.index": {"uri": "posts/{post}/comments", "methods": ["GET"]},
            "postComments.show": {
                "uri": "posts/{post}/comments/{comment}",
                "methods": ["GET"],
            },
            "admin.users.index": {"uri": "admin/users", "methods": ["GET"]},
        }
        self.assertEqual(expected, routes)

    def test_returns_unfiltered_routes_when_both_only_and_except_configs_set(self):
        FILTERS["except"] = ["posts.s*", "home"]
        FILTERS["only"] = ["some.other.routes"]

        routes = JsRoutes().to_dict()["routes"]
        self.assertEqual(all_expected_routes, routes)

    def test_can_set_included_routes_using_groups_config(self):
        FILTERS["groups"] = {"posts": ["posts.s*"]}
        routes = JsRoutes("posts").to_dict()["routes"]
        expected = {
            "posts.show": {"uri": "posts/{post}", "methods": ["GET"]},
            "posts.store": {"uri": "posts", "methods": ["POST"]},
        }
        import pdb

        pdb.set_trace()
        self.assertEqual(expected, routes)

    def test_can_set_included_routes_using_groups_array_config(self):
        FILTERS["groups"] = {"posts": ["posts.s*"], "admin": ["admin.*"]}
        routes = JsRoutes(["posts", "admin"]).to_dict()["routes"]
        expected = {
            "posts.show": {"uri": "posts/{post}", "methods": ["GET"]},
            "posts.store": {"uri": "posts", "methods": ["POST"]},
            "admin.users.index": {"uri": "admin/users", "methods": ["GET"]},
        }
        import pdb

        pdb.set_trace()
        self.assertEqual(expected, routes)

    def can_ignore_passed_group_not_set_in_config(self):
        FILTERS["groups"] = {"posts": ["posts.s*"]}
        routes = JsRoutes(["unknown_group"]).to_dict()["routes"]
        self.assertEqual(all_expected_routes, routes)

    def can_include_middleware(self):
        pass

    def can_include_only_middleware_set_in_config(self):
        pass
