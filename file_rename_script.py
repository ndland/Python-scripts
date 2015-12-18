#!/usr/local/opt/coreutils/libexec/gnubin/env python3

import os, time
from datetime import datetime

current_directory = os.listdir(os.getcwd())
files = [f for f in current_directory if os.path.isfile(f)]

for file in files:
    file_name, file_extension = os.path.splitext(file)
    create_date = datetime.fromtimestamp(os.path.getctime(file)).strftime('%Y_%m_%d')
    prompt_user = "What would you like to name " + file + " to? "
    user_response = input(prompt_user)
    if user_response:
        os.rename(file, create_date + "-" + user_response.replace(" ", "_") + file_extension)
        print("Renamed your file to", create_date + "-" + user_response.replace(" ", "_") + file_extension)
        print()
    else:
        print(file, "was not changed")
        print()
