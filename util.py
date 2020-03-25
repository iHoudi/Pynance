from os import name, system, path, getcwd, mkdir, listdir
from time import sleep
from colorama import Fore

import json
import ntpath
import platform

keys = ["name_l", "name_f", "account_id", "date",
        "old_bal", "deposit", "withdraw", "updated_bal", ]

fields = ["Last Name: ", "First Name: ", "Account ID: ",
          "Date (mm/dd/yy): ", "Current Balance($): ", "Deposit($): ", "Withdraw(S): ", "New Balance($): "]

repo1 = {}
repo2 = {}
repo3 = {}
repo4 = {}
repo5 = {}

repos = {1: repo1, 2: repo2, 3: repo3, 4: repo4, 5: repo5}

colors = {1: Fore.RED, 2: Fore.GREEN, 3: Fore.YELLOW,
          4: Fore.LIGHTGREEN_EX, 5: Fore.CYAN, 6:
          Fore.MAGENTA}

menu_options = {0: "L >> Load JSON",
                1: "C >> Create JSON", 2: "E >> Exit"}


header = "+-------" + Fore.GREEN + "Pynance" + Fore.RESET + "-------+"
header_c = "+-------Pynance-------+"
footer = "+-----------------------+"

def return_check():

    with open('check.json') as _json:

        data = json.load(_json)
        check_stat = data['check']

        _json.close()

        if check_stat == 0:
            check_set_t(data)

    return check_stat


def check_set_t(data):
    data['check'] = 1

    _json = open("check.json", "w")

    json.dump(data, _json)


def get_file_path():
    _dir = getcwd()
    if getOS() == "Windows":
        json_dir = path.join(_dir, "jsons\\")
    else: 
        json_dir = path.join(_dir, "jsons/")

    if not json_dir:
        mkdir(json_dir)

    return json_dir


def lfile_path(path):
    if getOS() == 'Windows':
        _dir = getcwd() + "\\jsons\\" + path
    else:
        _dir = getcwd() + "/jsons/" + path

    return _dir


def _filesInDir():
    di = getcwd()
    if getOS() == 'Windows':
        total = di + "\\jsons"
    else: 
        total = di + "/jsons"
    return listdir(total)


def wait(time):
    sleep(time)

def getOS():
    return platform.system()

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        print(name)
        _ = system('clear')

def fcolor(color_val, text):

    return colors[color_val] + text
