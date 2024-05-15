# ADMIN FILE


# Kellan Yamamoto
# 28388886
# kellany@uci.edu

from pathlib import Path
import ui as ui
import a3 as a3

admin_instructions = """Print Full File using syntax:
[COMMAND] [INPUT] [[-]OPTION] [INPUT]
-------------------------------------
"""


def start():
    print("ADMIN MODE ENABLED")
    print(admin_instructions)
    ui.adminis(1)
    ui.commands()
