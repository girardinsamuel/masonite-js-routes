# flake8: noqa F811
from masonite.tests import TestCase
from masonite.routes import Route
from masonite.configuration import config
from masonite.facades import Config

from src.masonite.js_routes.routes import Routes as JsRoutes

all_expected_routes = {
    "home": {"uri": "home", "methods": ["GET"], "bindings": {}},
    "posts.show": {"uri": "posts/{post}", "methods": ["GET"], "bindings": {}},
    "posts.store": {"uri": "posts", "methods": ["POST"], "bindings": {}},
    "posts.index": {"uri": "posts", "methods": ["GET"], "bindings": {}},
    "postComments.index": {
        "uri": "posts/{post}/comments",
        "methods": ["GET"],
        "bindings": {},
    },
    "postComments.show": {
        "uri": "posts/{post}/comments/{comment}",
        "methods": ["GET"],
        "bindings": {},
    },
    "admin.users.index": {"uri": "admin/users", "methods": ["GET"], "bindings": {}},
}


class TestRoutes(TestCase):
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
        self.original_config = {
            "filters": {"only": [], "except": [], "groups": {}},
            "skip_route_function": False,
        }

    def tearDown(self):
        super().tearDown()
        Config.set("js_routes", self.original_config)

    def test_basic_routes_generation(self):
        js_routes = JsRoutes()
        routes = js_routes.routes
        self.assertEqual(all_expected_routes, routes)

    def test_can_filter_to_only_include_routes_matching_a_pattern(self):
        js_routes = JsRoutes()
        routes = js_routes.filter_routes(["posts.s*", "home"])
        expected = {
            "home": {"uri": "home", "methods": ["GET"], "bindings": {}},
            "posts.show": {"uri": "posts/{post}", "methods": ["GET"], "bindings": {}},
            "posts.store": {"uri": "posts", "methods": ["POST"], "bindings": {}},
        }
        self.assertEqual(expected, routes)

    def test_can_filter_to_exclude_routes_matching_a_pattern(self):
        js_routes = JsRoutes()
        routes = js_routes.filter_routes(["posts.s*", "home", "admin.*"], False)
        expected = {
            "posts.index": {"uri": "posts", "methods": ["GET"], "bindings": {}},
            "postComments.index": {
                "uri": "posts/{post}/comments",
                "methods": ["GET"],
                "bindings": {},
            },
            "postComments.show": {
                "uri": "posts/{post}/comments/{comment}",
                "methods": ["GET"],
                "bindings": {},
            },
        }

        self.assertEqual(expected, routes)

    def test_can_set_included_routes_using_only_config(self):
        Config.set("js_routes.filters.only", ["posts.s*", "home"])
        routes = JsRoutes().to_dict()["routes"]
        expected = {
            "home": {"uri": "home", "methods": ["GET"], "bindings": {}},
            "posts.show": {"uri": "posts/{post}", "methods": ["GET"], "bindings": {}},
            "posts.store": {"uri": "posts", "methods": ["POST"], "bindings": {}},
        }
        self.assertEqual(expected, routes)

    def test_can_set_included_routes_using_except_config(self):
        Config.set("js_routes.filters.except", ["posts.s*", "home"])
        routes = JsRoutes().to_dict()["routes"]
        expected = {
            "posts.index": {"uri": "posts", "methods": ["GET"], "bindings": {}},
            "postComments.index": {
                "uri": "posts/{post}/comments",
                "methods": ["GET"],
                "bindings": {},
            },
            "postComments.show": {
                "uri": "posts/{post}/comments/{comment}",
                "methods": ["GET"],
                "bindings": {},
            },
            "admin.users.index": {
                "uri": "admin/users",
                "methods": ["GET"],
                "bindings": {},
            },
        }
        self.assertEqual(expected, routes)

    def test_returns_unfiltered_routes_when_both_only_and_except_configs_set(self):
        Config.set(
            "js_routes.filters",
            {"except": ["posts.s*", "home"], "only": ["some.other.routes"], "groups": []},
        )
        routes = JsRoutes().to_dict()["routes"]
        self.assertEqual(all_expected_routes, routes)

    def test_can_set_included_routes_using_groups_config(self):
        Config.set("js_routes.filters.groups", {"posts": ["posts.s*"]})
        self.application.bind("config.js_routes", "tests.unit.test_routes")
        routes = JsRoutes("posts").to_dict()["routes"]
        expected = {
            "posts.show": {"uri": "posts/{post}", "methods": ["GET"], "bindings": {}},
            "posts.store": {"uri": "posts", "methods": ["POST"], "bindings": {}},
        }
        self.assertEqual(expected, routes)

    def test_can_set_included_routes_using_groups_array_config(self):
        Config.set("js_routes.filters.groups", {"posts": ["posts.s*"], "admin": ["admin.*"]})
        routes = JsRoutes(["posts", "admin"]).to_dict()["routes"]
        expected = {
            "posts.show": {"uri": "posts/{post}", "methods": ["GET"], "bindings": {}},
            "posts.store": {"uri": "posts", "methods": ["POST"], "bindings": {}},
            "admin.users.index": {
                "uri": "admin/users",
                "methods": ["GET"],
                "bindings": {},
            },
        }
        self.assertEqual(expected, routes)

    def can_ignore_passed_group_not_set_in_config(self):
        Config.set("js_routes.filters.groups", {"posts": ["posts.s*"]})
        routes = JsRoutes(["unknown_group"]).to_dict()["routes"]
        self.assertEqual(all_expected_routes, routes)

    def can_include_middleware(self):
        pass

    def can_include_only_middleware_set_in_config(self):
        pass
