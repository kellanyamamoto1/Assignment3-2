'''
Modified given file to connect to server
'''
# Starter code for assignment 3 in ICS 32 Programming with Software
# Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886

import socket
import json
import ds_protocol
import time
SERVER_ADDRESS = "168.235.86.101"
SERVER_PORT = 3021
TIMESTAMP = str(time.time())


def send(
        server: str,
        port: int,
        username: str,
        password: str,
        message: str,
        bio: str = None):
    '''
    The send function joins a ds server and sends a message, bio, or both

    :param server: The ip address for the ICS 32 DS server.
    :param port: The port where the ICS 32 DS server is accepting connections.
    :param username: The user name to be assigned to the message.
    :param password: The password associated with the username.
    :param message: The message to be sent to the server.
    :param bio: Optional, a bio for the user.
    '''

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_conn:
            server_conn.connect((server, port))
            stuff = {}
            stuff["join"] = {
                "username": username,
                "password": password,
                "token": ""
            }
            print("joined")
            data_str = json.dumps(stuff)
            server_conn.sendall(data_str.encode())
            response = server_conn.recv(3021).decode()
            response_json = json.loads(response)
            print(response_json)
            if "token" in str(response_json):
                temp = str(response_json).index("token")
                token = str(response_json)[temp + 9:-3]
            if message:
                action = "post"
                formatted_message = ds_protocol.format_for_json(
                    action, username, password, user_token=token,
                    message=message, bio=bio)
                print(formatted_message)
            elif bio:
                action = "bio"
                formatted_message = ds_protocol.format_for_json(
                    action, username, password, user_token=token,
                    message=message, bio=bio)
                print(formatted_message)
            else:
                action = "join"
                formatted_message = ds_protocol.format_for_json(
                    action, username, password, user_token=token,
                    message=message, bio=bio)
                print(formatted_message)
            formatted_message = ds_protocol.format_for_json(
                action, username, password, user_token=token,
                message=message, bio=bio)
            print(formatted_message)
            data_str = json.dumps(formatted_message)
            print(f"{data_str}")
            server_conn.sendall(data_str.encode())

            response = server_conn.recv(3021).decode()
            response_json = json.loads(response)
            print(response_json)
            if "response" in response_json:
                if response_json["response"]["type"] == "ok":
                    return True
                else:
                    error_message = response_json["response"]["message"]
                    print("Error:", error_message)
                    return False
            else:
                print("Invalid response from server")
                return False
    except Exception as exerr:
        print(f"there was an error:  {exerr}")
    return
