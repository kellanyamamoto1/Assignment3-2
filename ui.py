# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software
# Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886

import pathlib
from pathlib import Path
from Profile import Profile, Post
import ui as ui
import admin as admin
import user as user
administrator = False
temp_path = ''

command_list = """
Q -- Quit the program
C -- Create a new file in a specified path
D -- Deleted a file
R -- Read a file
O -- Open a file
E -- Edit a file
P -- Print a file
*To edit or print the contents of a file, you must
    open it first using the O command
(Syntax - 'O [path]' inlcuding the file and extension)
*If user, use syntax:[COMMAND] [[-]OPTION]")
"""


def commands():
    print(command_list)
    user_input = input("Input command with path and desired file: ").split(" ")
    command = user_input[0]
    directory = user_input[1] if len(user_input) > 1 else None
    options = user_input[2] if len(user_input) > 2 else None
    name = user_input[3] if len(user_input) > 3 else None
    if command == "admin":
        admin.start()
    else:
        if command == 'Q':
            print("Quitting the program.")
            quit()
        elif command == 'R':
            if directory:
                read_file(directory)
            else:
                print("ERROR")
        elif command == 'C':
            create_file(user_input)
        elif command == 'D':
            if directory:
                delete_file(directory)
        elif command == 'O':
            if directory:
                open_file(directory)
            else:
                print("ERROR")
        elif command == 'E':
            edit_file(" ".join(user_input))
        elif command == 'P':
            print_file_data(" ".join(user_input))


def user_check():
    user_type = input("admin or user?: ")
    temp = 0
    if user_type == "admin":
        temp = 1
    else:
        temp = 0
    return temp


def adminis(num):
    global administrator
    if num == 1:
        administrator = True
    else:
        administrator = False
    return administrator


"""
- Create file - fix admin
- Edit file - updated values are fucked up
- check for admin in all sections
- style checker
"""


def get_path():
    print("Please enter a path")
    path = input()
    path = path + '\\'
    return path


def file_name():
    name = input("Please enter a file name without file extenstion:")
    return name


def open_file(file_path):
    global temp_path
    if administrator:
        path = file_path.split(' ')
        temp_path = file_path
        f = open(temp_path, 'a')
        print(temp_path + " has been opened as administrator")
        return temp_path
    else:
        path = get_path()
        print("With the file extention,")
        name = file_name()
        temp_path = path + name + '.dsu'
        f = open(temp_path, 'r')
        print(temp_path + ' Has been opened')
        print(f.read())
    commands()
    return temp_path


def edit_file(user_input):
    get_path()
    print("To use 'E', use syntax: 'E [-]OPTION] [INPUT] ")
    lisp = user_input
    bio_index = lisp.find('-bio')
    bio = lisp[bio_index + 1]
    if bio_index != -1:
        start_quote = user_input.find('"', bio_index)
        end_quote = user_input.find('"', start_quote + 1)
        if start_quote != -1 and end_quote != -1:
            bio = user_input[start_quote + 1:end_quote]

    profile = Profile()
    profile.load_profile(path=temp_path)

    if '-usr' in lisp:
        usr_index = lisp.index('-usr')
        new_usr = ' '.join(lisp[usr_index + 1:]).strip('"')
        profile.username = new_usr
        profile.save_profile(temp_path)
        print("username updated")
    if '-pwd' in lisp:
        pwd_index = lisp.index('-pwd')
        new_pwd = lisp[pwd_index + 1]
        profile.password = new_pwd.strip('"')
        profile.save_profile(temp_path)
        print("password updated")
    if '-bio' in lisp:
        profile.bio = bio.strip('"')
        profile.save_profile(path=temp_path)
        print("bio updated")
    if '-addpost' in lisp:
        post_index = lisp.index('-addpost')
        post_content = ' '.join(lisp[post_index + 1:])
        new_post = Post(post_content)
        profile.add_post(new_post)
        profile.save_profile(temp_path)
        print("post added")
    if '-delpost' in lisp:
        del_index = lisp.index('-delpost')
        del_content = ''.join(lisp[del_index + 1:])
        profile.del_post(del_content)
        print("Post Deleted")
    commands()


def print_file_data(user_input):
    options = user_input.split()[1:]

    global temp_path
    profile = Profile()
    profile.load_profile(temp_path)

    if '-usr' in options:
        print("Username:", profile.username)
    if '-pwd' in options:
        print("Password:", profile.password)
    if '-bio' in options:
        print("Bio:", profile.bio)
    if '-posts' in options:
        for i, post in enumerate(profile._posts):
            print(f"Post {i}: {post}")
    if '-post' in options:
        post_index = options.index('-post')
        post_id = int(options[post_index + 1])
        if 0 <= post_id < len(profile._posts):
            print(f"Post {post_id}: {profile._posts[post_id]}")
        else:
            print("Invalid post ID")
    if '-all' in options:
        print("Username:", profile.username)
        print("Password:", profile.password)
        print("Bio:", profile.bio)
        print("Posts:")
        for i, post in enumerate(profile._posts):
            print(f"  Post {i}: {post}")
    commands()

    pass


def create_file(user_input):
    global temp_path
    items = user_input
    if administrator:
        paths = items
        if len(paths) > 1:
            path = paths[1]
            if '-n' in paths:
                n_index = paths.index('-n')
                temp = n_index + 1
                fileName = paths[temp]
                file_ext = fileName + '.dsu'
                filepath = Path(path) / file_ext
                username = input("Enter username: ")
                password = input("Enter password: ")
                bio = input("Enter Bio: ")
                profile = Profile(
                    username=username, password=password, bio=bio)
                with open(filepath, 'a') as f:
                    print("")
                f = open(filepath, 'a')
                profile.save_profile(path=filepath)
                print(f'{filepath} OPENED')
                temp_path = filepath
            else:
                print("[COMMAND] [INPUT] [[-]OPTION] [INPUT] syntax")
        print(f"PATH TO FILE:  {temp_path}")
        commands()
        return temp_path
    else:
        if '-n' in items:
            the_path = get_path()
            the_name = file_name()
            line = the_path + "\\" + the_name + ".dsu"
            username = input("Enter Username:  ")
            password = input("Enter Password:  ")
            bio = input("Enter bio: ")
            profile = Profile(username=username, password=password, bio=bio)
            print(line + "      CREATED")
            with open(line, 'a') as f:
                u = "Username: " + username + '\n'
                f.write(u)
                p = "Password: " + password + '\n'
                f.write(p)
                b = "Bio: " + bio + '\n'
                f.write(b)
            profile.save_profile(path=line)
            f = open(line, 'a')
        else:
            print("Must follow: [COMMAND] [[-]OPTION]syntax ")
    commands()
    return temp_path


def delete_file(file_path):
    suffix = ".dsu"
    if file_path.endswith(suffix):
        path = pathlib.Path(file_path)
        if path.exists():
            path.unlink()
            print(f"{file_path} DELETED")
            commands()
        else:
            print(f"File '{file_path}' not found")
    else:
        print("File in directory not found")


def read_file(file_path):
    if file_path.endswith('.dsu'):
        path = pathlib.Path(file_path)
        if path.exists() and path.is_file():
            with open(path, 'r') as file:
                content = file.read()[:-1]
                if not content:
                    print("EMPTY")
                else:
                    print(content)
        else:
            print(f"File '{file_path}' not found")
    else:
        print("ERROR")
