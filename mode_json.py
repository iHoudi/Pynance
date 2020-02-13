import json


def json_main():
    # This either calls upon load_json or create_json
    mode = str(input(
        "Do you want to create a json or load a json? (y/n) >> ").lower())
    if mode == "y":
        person_dict = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'
        person = json.loads(person_dict)

        with open('person.json', 'w') as json_file:
            json.dump(person, json_file)
            print(json.dumps(person, indent=4, sort_keys=True))

    elif mode == "n":
        print("No")
    else:
        print("Input invalid")


def load_json(file):
    return file + "HELLO"
