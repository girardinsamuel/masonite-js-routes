"""CreateProfiles Migration."""

from masoniteorm.migrations import Migration


class CreateProfiles(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("profiles") as table:
            table.increments("id")
            table.integer("user_id")
            table.string("avatar").nullable()
            table.string("role")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("profiles")
