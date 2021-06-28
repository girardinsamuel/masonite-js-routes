from masonite.providers import (
    RouteProvider,
    FrameworkProvider,
    ViewProvider,
    WhitenoiseProvider,
    ExceptionProvider,
    MailProvider,
    SessionProvider,
    QueueProvider,
    CacheProvider,
    EventProvider,
    StorageProvider,
    HelpersProvider,
    BroadcastProvider,
    AuthenticationProvider,
)

# register local package
from src.masonite.js_routes import JSRoutesProvider

PROVIDERS = [
    FrameworkProvider,
    HelpersProvider,
    JSRoutesProvider,
    RouteProvider,
    ViewProvider,
    WhitenoiseProvider,
    ExceptionProvider,
    MailProvider,
    SessionProvider,
    CacheProvider,
    QueueProvider,
    EventProvider,
    StorageProvider,
    BroadcastProvider,
    AuthenticationProvider,
]
