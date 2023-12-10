import base64

from messageValidator import check_message_validity


def ingest_message(event, context):
    message = base64.b64decode(event['data']).decode('utf-8')

    print(f"A new login message is received: {message}")

    is_valid_message = check_message_validity(message)
    print(f"Message is valid: {is_valid_message}")
