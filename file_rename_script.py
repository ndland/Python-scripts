#!/usr/local/opt/coreutils/libexec/gnubin/env python3

import os
import time
import sys
from datetime import datetime


def main(arg):
    if len(sys.argv) > 1:
        rename_file(sys.argv[1])
    else:
        current_directory = os.listdir(os.getcwd())
        files = [f for f in current_directory if not f.startswith('.') and os.path.isfile(f)]
        for file in files:
            rename_file(file)


def set_up_file_name(file):
    file_name, file_extension = os.path.splitext(file)
    create_date = datetime.fromtimestamp(
        os.path.getctime(file)).strftime('%Y_%m_%d')
    return file_name, file_extension, create_date


def prompt_user_for_name(file):
    prompt_user = "What would you like to name " + file + " to? "
    user_response = input(prompt_user)
    return user_response


def rename_file(file):
    file_name, file_extension, create_date = set_up_file_name(file)
    user_response = prompt_user_for_name(file)
    if user_response:
        os.rename(file, create_date + "-" + user_response.replace(" ",
                                                                  "_").replace("~", "-").lower() + file_extension)
        print("Renamed your file to", create_date + "-" +
              user_response.replace(" ", "_").replace("~", "-").lower() + file_extension)
        print()
    else:
        print(file, "was not changed")
        print()


if __name__ == '__main__':
    main(sys.argv[1:])
