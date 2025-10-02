from localstack.pro.core.services.appsync.event_api.message_processors.connection import (
    ConnectionInitProcessor,
)
from localstack.pro.core.services.appsync.event_api.message_processors.publish import (
    PublishMessageProcessor,
)
from localstack.pro.core.services.appsync.event_api.message_processors.subscription import (
    SubscribeProcessor,
    UnsubscribeProcessor,
)

MESSAGE_PROCESSOR_MAPPING = {
    ConnectionInitProcessor.message_type: ConnectionInitProcessor(),
    PublishMessageProcessor.message_type: PublishMessageProcessor(),
    SubscribeProcessor.message_type: SubscribeProcessor(),
    UnsubscribeProcessor.message_type: UnsubscribeProcessor(),
}

__all__ = [
    "MESSAGE_PROCESSOR_MAPPING",
]
