from cleo import Command
from masonite.utils.filesystem import make_directory

from ..generator import RoutesGenerator


class GenerateCommand(Command):
    """
    Generate routes.js file

    js_routes:generate
        {--p|--path=resources/js/routes.js : Output file path from root}
    """

    def handle(self):
        if self.option("path"):
            default_path = self.option("path")
        else:
            default_path = "resources/js/routes.js"
        self.info("Start generating JS Routes...")
        generator = RoutesGenerator()
        file_content = generator.generate_for_file()
        make_directory(default_path)
        with open(default_path, "w") as f:
            f.write(file_content)
        self.info("routes file has been generated at {0}!".format(default_path))
