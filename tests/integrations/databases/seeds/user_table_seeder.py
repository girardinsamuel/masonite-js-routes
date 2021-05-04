"""User Table Seeder.
You can run this seeder in order to generate users.
    - Each time it is ran it will generate 50 random users.
    - All users have the password of 'secret'.
    - You can run the seeder by running: craft seed:run.
"""
import random
from masoniteorm.seeds import Seeder

from ...app.User import User
from ...app.Profile import Profile
from config.factories import factory


class UserTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        users = factory(User, 50).create()
        for u in User.all():
            Profile.create(
                {
                    "user_id": u.id,
                    "role": random.choice(["admin", "basic"]),
                    "avatar": f"https://randomuser.me/api/portraits/men/{u.id}.jpg",
                }
            )
