import base64

from persister import persistMessage


def ingest_message(event, context):
    message = base64.b64decode(event['data']).decode('utf-8')

    print(f"A new login message is received: {message}")

    persistMessage(message)
