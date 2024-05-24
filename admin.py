# ADMIN FILE


# Kellan Yamamoto
# 28388886
# kellany@uci.edu

"""
Module that processes the admin mode.
Will print the Admin syntax instructions
"""

import ui

ADMIN_INSTRUCTIONS = """Print Full File using syntax:
[COMMAND] [INPUT] [[-]OPTION] [INPUT]
-------------------------------------
"""


def start():
    """
    Function will start when program is initalized,
    will print telling the person admin mode is enabled
    """
    print("ADMIN MODE ENABLED")
    print(ADMIN_INSTRUCTIONS)
    ui.adminis(1)
    ui.commands()
