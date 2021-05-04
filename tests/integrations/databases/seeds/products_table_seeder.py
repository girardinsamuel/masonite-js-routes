"""ProductsTableSeeder Seeder."""
import random
from masoniteorm.seeds import Seeder
from ...app.Product import Product

from config.factories import factory


class ProductsTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        from .User import User

        # associate between 0 to 15 products for each user
        for user in User.all():
            count = random.randint(0, 15)
            factory(Product, count).create({"user_id": user.id})
