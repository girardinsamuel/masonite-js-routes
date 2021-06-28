from masonite.foundation import Application, Kernel
from tests.integrations.config.providers import PROVIDERS
import os

from tests.integrations.app.Kernel import Kernel as ApplicationKernel


application = Application(os.getcwd())

"""First Bind important providers needed to start the server
"""

application.register_providers(Kernel, ApplicationKernel)

application.add_providers(*PROVIDERS)
