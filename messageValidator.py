import json
import time


def login_timestamp_is_in_the_future(login_timestamp):
    return time.time() < login_timestamp


def check_message_validity(message: str) -> bool:
    json_message = json.loads(message)

    if json_message["client_id"] is None:
        return False
    if login_timestamp_is_in_the_future(json_message["login_timestamp"]):
        return False
    return True
