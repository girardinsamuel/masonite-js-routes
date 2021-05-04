"""Base Database Seeder Module."""
from masoniteorm.seeds import Seeder

from .products_table_seeder import ProductsTableSeeder
from .user_table_seeder import UserTableSeeder


class DatabaseSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        # self.call(UserTableSeeder)
        self.call(ProductsTableSeeder)