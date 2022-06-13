from masonite.controllers import Controller


class TestController(Controller):
    def show(self):
        return "test"
