import subprocess
import re

# run command to show all the profiles
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

# list the wifi names using regular expression
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

# final result of wifi name and password
wifi_list = []


if len(profile_names):
    for name in profile_names:

        # temp dict of current wifi profiles
        wifi_dict = {}

        # information of current wifi profile
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        
        # check if security key is present or not usign regular expression
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_dict["name"] = name
            
            # command for the password of wifi profiles/name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            
            # search the password usign regular expression
            password = re.search("Key Content            : (.*)\r", profile_info_pass)

            # check if password is found
            if password == None:
                wifi_dict["password"] = None
            else:
                wifi_dict["password"] = password[1]

            # append the dictionary in the list
            wifi_list.append(wifi_dict)

for result in wifi_list:
    char = 30
    name = result["name"]
    password = result["password"]

    space = (char - len(name)) * "-"

    print(f"{name} {space}> {password}")
