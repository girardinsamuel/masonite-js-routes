""" Web Routes """
from masonite.routes import Get


ROUTES = [
    Get('/app/', 'AppController@show').name('app'),
    Get('/welcome/', 'WelcomeController@show').name('welcome'),
    Get('/welcome/@user', 'WelcomeController@user').name('welcome.user'),
    Get('/welcome/?user', 'WelcomeController@user_or_anonymous').name('welcome.user_or_anonymous'),
    Get('/welcome/@user:string', 'WelcomeController@user_with_check').name('welcome.user_with_check'),
    # Get('/welcome/@user:int', 'WelcomeController@user_with_check').name('welcome.user_with_check'),
    Get('/welcome/@user1/and/@user2', 'WelcomeController@two_users').name('welcome.two_users'),
]
