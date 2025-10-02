from forwarder.sample_config import (
    Config,
)


class Development(Config):
    API_KEY = "XXXX"  # Your bot API key
    OWNER_ID = 488792444  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [
        -570374810
    ]  # List of chat id's to forward messages from.
    TO_CHATS = [
        -570374810
    ]  # List of chat id's to forward messages to.

    WORKERS = 4
