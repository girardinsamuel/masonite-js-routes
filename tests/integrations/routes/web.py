""" Web Routes """
from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show").name("home"),
    Route.get("posts", "WelcomeController@posts").name("posts.index"),
    Route.post("posts", "WelcomeController@create_post").name("posts.create"),
    # Route.match(["get", "post"], "posts", "WelcomeController@posts").name("posts"),
    Route.get("posts/@id", "WelcomeController@show_post").name("posts.show"),
    Route.get("posts/@post_id/comments/@id", "WelcomeController@show_post_comments").name(
        "posts.comments.show"
    ),
]
