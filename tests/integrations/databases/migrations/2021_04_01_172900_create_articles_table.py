"""CreateArticlesTable Migration."""

from masoniteorm.migrations import Migration


class CreateArticlesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("articles") as table:
            table.increments("id")
            table.string("title")
            table.text("description").nullable()
            table.integer("author_id")
            table.boolean("published")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        pass
