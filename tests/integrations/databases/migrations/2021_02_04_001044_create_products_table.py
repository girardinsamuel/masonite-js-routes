"""CreateProductsTable Migration."""

from masoniteorm.migrations import Migration


class CreateProductsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("products") as table:
            table.increments("id")
            table.string("name")
            table.boolean("published")
            table.integer("user_id")
            table.string("reference").unique()
            table.text("description").nullable()
            table.decimal("price_ht")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("products")
