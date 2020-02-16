import json
import ntpath


def file_selector():
    print("0 = Load JSON,\n1 = Load CSV,\n2 = Load text file")
    _format = int(input("Mode: "))
    if _format == 0:
        mode_json()
    elif _format == 1:
        print()
    elif _format == 2:
        print()
    else:
        print()


def mode_json():

    # asks for path of json
    # load a json
    # populate local variables with json
    # allow for ediitng of the loaded json
    # export the json

    try:
        # locates json

        print("What is the file path for your exisiting JSON? >>")
        path = str(input("Path: "))

        # strips the path provided down to the file name and type
        path_tail = ntpath.basename(path)

        # attempts to load json file and print contents

        with open(path_tail) as _json:
            data = json.load(_json)

            # print(json.dumps(data, indent=4))

        for account in data['statement']:
            print("+-------------------------------------+")
            print(account['name_f'], account['name_l'])
            print("Account_id:", account['account_id'])
            print("Date>>", account['date'])
            print("Previous Balance>>", f"${account['old_bal']}")
            print("Deposit>>", f"${account['deposit']}")
            print("Withdraw>>", f"${account['withdraw']}")
            print("Update Balance>>", f"${account['updated_bal']}\n")

    except Exception:
        print("Invalid Input or JSON Error")
