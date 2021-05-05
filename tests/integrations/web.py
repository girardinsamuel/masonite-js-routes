""" Web Routes """
from masonite.routes import Route

Route.get("/", "WelcomeController@show").name("home"),
Route.get("posts", "WelcomeController@posts").name("posts.index"),
Route.get("posts/@id", "WelcomeController@show_post").name("posts.show"),
