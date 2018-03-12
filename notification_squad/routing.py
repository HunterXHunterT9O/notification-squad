from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import notifications.routing

ASGI_APPLICATION = "notification_squad.routing.application"

application = ProtocolTypeRouter()
