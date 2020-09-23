""" Web Routes """
from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'MasoniteJSRoutesController@show').name('welcome'),
]
