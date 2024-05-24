'''
Modified given file to connect to server
'''
# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software
# Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886

import json
import time
from collections import namedtuple

DataTuple = namedtuple('DataTuple', ['foo', 'baz'])
TIMESTAMP = str((time.time()))


def extract_json(json_msg: str) -> DataTuple:
    '''
    Call the json.loads function on a json
    string and convert it to a DataTuple object
    '''
    try:
        json_obj = json.loads(json_msg)
        foo = json_obj['foo']
        baz = json_obj['bar']['baz']
    except json.JSONDecodeError:
        print("Json cannot be decoded.")

    return DataTuple(foo, baz)


def format_for_json(
        action_type,
        username,
        password,
        user_token=None,
        message=None,
        bio=None):
    """
    Formats the JSON file
    """
    formated = None
    if action_type == "join":
        formated = json.dumps({
            "join": {
                "username": username,
                "password": password,
                "tokens": user_token
            }
        })
    elif action_type == 'post':
        if not user_token:
            raise ValueError("no user token")
        formated = ({
            "token": user_token,
            "post": {
                "entry": message,
                "timestamp": TIMESTAMP
            }
        })
    elif action_type == 'bio':
        if not user_token:
            raise ValueError("Value Error")
        formated = json.dumps({
            "token": user_token,
            "bio": {
                "entry": bio,
                "timestamp": TIMESTAMP
            }
        })

    return formated
