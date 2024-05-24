"""
Main file that begins program which will run admin,
user, and trigger the UI
"""
# a3.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886


import ui
import admin
import user

# PATH: C:\Users\kella\OneDrive\Desktop\ICS32Again\Assignment3
# E -usr "mark b" -pwd "password123" -bio "test bio"

if __name__ == "__main__":
    if ui.user_check() == 1:
        admin.start()
    else:
        # print list of commands
        user.start()
