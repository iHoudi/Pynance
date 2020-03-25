import json
import util
import os


def load_json():

    _run = True

    try:
        print(util._filesInDir())
        #print(os.getcwd())
        print(util.fcolor(5,"Which file would you like to load?"))
        path = str(input(util.fcolor(5,">> ")))

        # attempts to load json file and print contents
        print(util.fcolor(5, "Attempting To Read File"))
        print("file path >> " + util.lfile_path(path))
        with open(util.lfile_path(path)) as _json:
            print(util.fcolor(2, "Successful Read"))
            data = json.load(_json)

        for statement in data['statements']:
            info_access = statement['info']
            try:
                if _run != False:
                    print(util.header)
                for i in range(0, 8):
                    value = info_access[util.keys[i]]
                    print(util.fields[i], value)
                print(f"{util.footer}\n")
                util.wait(3)
                _run = False
            except Exception:
                #print(util.fcolor(1, "ERROR"))
                break
            continue

    except Exception:
        print(util.fcolor(1, "Invalid Path OR JSON Read Error"))
        util.wait(1.5)
        # util.clear()
