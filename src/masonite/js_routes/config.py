""" Masonite JS Routes Settings """

"""
|--------------------------------------------------------------------------
| Filters
|--------------------------------------------------------------------------
|
| Filtering routes is completely optional. If you want to pass all of your routes to your
| JavaScript by default, let the default values.
| You can either define 'only' or 'except' with a list of route name patterns.
| You can also optionally define multiple groups of included routes using 'groups' key.
|
|
"""
FILTERS = {"only": [], "except": [], "groups": {}}
# FILTERS = {
#     "only": ["home", "api.*"],
#     "except": ["debugbar.*", "horizon.*", "admin.*"],
#     "groups": {
#         "admin": ["admin.*", "posts.*"],
#         "author": ["posts.*"]
#     }
# }

"""
|--------------------------------------------------------------------------
| Skip JS route() function
|--------------------------------------------------------------------------
|
| If you only want to use the @routes directive to make your app's routes available in JavaScript,
| but don't need the route() helper function, you can set this parameter to True.
|
"""
SKIP_ROUTE_FUNCTION = False
