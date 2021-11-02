from masonite.foundation import Application, Kernel

from tests.integrations.config.providers import PROVIDERS
from tests.integrations.Kernel import Kernel as ApplicationKernel


application = Application("tests/integrations")

"""First Bind important providers needed to start the server
"""

application.register_providers(Kernel, ApplicationKernel)

application.add_providers(*PROVIDERS)
