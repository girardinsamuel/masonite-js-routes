from masonite.tests import TestCase
from src.masonite.js_routes.helpers import matches


class TestHelpers(TestCase):
    sqlite = False

    def test_no_matches_when_no_pattern(self):
        self.assertEqual(False, matches(None, "api"))
        self.assertEqual(False, matches([], "api"))
        self.assertEqual(False, matches("", "api"))
        self.assertEqual(False, matches("", ""))

    def test_matches_exact_pattern(self):
        self.assertEqual(True, matches("api", "api"))
        self.assertEqual(True, matches(["api", "home"], "api"))

    def test_no_matches_with_pattern(self):
        self.assertEqual(False, matches("home", "admin"))
        self.assertEqual(False, matches(["api", "home"], "admin"))

    def test_matches_with_wildcards(self):
        self.assertEqual(True, matches("us*", "users"))
        self.assertEqual(True, matches("users*", "users"))

        self.assertEqual(True, matches("users.*", "users.list"))
        self.assertEqual(True, matches("users.*", "users.show"))
        self.assertEqual(False, matches("users.*", "users"))
        self.assertEqual(True, matches("users.*", "users.index.comments"))

        self.assertEqual(True, matches("users.s*", "users.store"))
        self.assertEqual(True, matches("users.s*", "users.show"))

        self.assertEqual(True, matches("api.*.index", "api.users.index"))
        self.assertEqual(True, matches("api.*.index", "api.admin.index"))
        self.assertEqual(False, matches("api.*.index", "api.users.logout"))
        self.assertEqual(True, matches("api.*.", "api.users.index"))
        self.assertEqual(True, matches("api.*.", "api.users.list"))
        self.assertEqual(False, matches("api.*.", "api.users"))

    def test_matches_with_wildcards_with_slash(self):
        self.assertEqual(True, matches("users/*", "users/1/comments"))
        self.assertEqual(True, matches("users/*/comments", "users/1/comments"))
        self.assertEqual(True, matches("users/*/comments", "users/4/comments"))

    def test_matches_with_wildcards_array(self):
        self.assertEqual(True, matches(["users.d*", "users.s*"], "users.show"))
        self.assertEqual(True, matches(["users.d*", "users.s*"], "users.delete"))
        self.assertEqual(False, matches(["users", "users.s*"], "users.delete"))

    def test_matches_with_multiple_wildcards(self):
        self.assertEqual(True, matches("users.s*.a*", "users.show.accounts"))
        self.assertEqual(True, matches("users.s*.a*", "users.store.accounts"))
        self.assertEqual(True, matches("users.s*.a*", "users.store.asomething"))
