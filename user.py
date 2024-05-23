# Kellan Yamamoto
# 28388886
# kellany@uci.edu

from pathlib import Path
import admin as admin
import ui as ui


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
