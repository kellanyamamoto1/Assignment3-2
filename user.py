# Kellan Yamamoto
# 28388886
# kellany@uci.edu
'''
user module
'''

from pathlib import Path
import ui


def check_file(user_input):
    """
    Checks if file exists in path
    """
    if Path(user_input).exists():
        return True
    else:
        return False


def start():
    """
    starts whole thing
    """
    ui.adminis(0)
    ui.commands()
