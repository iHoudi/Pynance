import json


def make_json():

    keys = ["name_l", "name_f", "account_id", "date",
            "old_bal", "deposit", "withdraw", "updated_bal", ]

    fields = ["last Name: ", "first Name: ", "account id: ",
              "date: ", "current Balance: ", "deposit: ", "withdraw: "]

    repo = {}
    statement_info = [repo]
    wrapper = {"statement": statement_info}

    for i in range(0, 8):
        if i <= 2:
            response = input(fields[i])
            repo.update({keys[i]: response})
        elif i > 2 and i < 7:
            print(i)
            response = int(input(fields[i]))
            repo.update({keys[i]: response})
        elif i == 7:
            old_bal = int(repo.get('old_bal'))
            deposit = int(repo.get('deposit'))
            withdraw = int(repo.get('withdraw'))

            updated_bal = (old_bal + deposit) - withdraw
            repo.update({keys[7]: updated_bal})

    with open('statments.json', 'w') as json_file:
        json.dump(wrapper, json_file, indent=4, sort_keys=False)

    for response in range(0, 7):
        # print(responses[response])
        print(keys[response], repo.get(keys[response]))

    print("Creating new file...")
