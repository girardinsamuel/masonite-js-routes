""" Web Routes """
from masonite.routes import Route

Route.get("/", "WelcomeController@show").name("welcome"),
