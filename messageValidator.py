import json
import time

VALID_MESSAGE = 0
NULL_CLIENT_ID = 1
INVALID_LOGIN_TIMESTAMP = 2


def login_timestamp_is_in_the_future(login_timestamp):
    return time.time() < login_timestamp


def check_message_validity(message: str) -> (bool, int):
    json_message = json.loads(message)

    if json_message["client_id"] is None:
        return False, NULL_CLIENT_ID
    if login_timestamp_is_in_the_future(json_message["login_timestamp"]):
        return False, INVALID_LOGIN_TIMESTAMP
    return True, VALID_MESSAGE


def get_output_message(message, reason):
    json_message = json.loads(message)
    if reason == VALID_MESSAGE:
        return json_message
    elif reason == NULL_CLIENT_ID:
        json_message["reason"] = "NULL_CLIENT_ID"
        return json_message
    elif reason == INVALID_LOGIN_TIMESTAMP:
        json_message["reason"] = "INVALID_LOGIN_TIMESTAMP"
        return json_message