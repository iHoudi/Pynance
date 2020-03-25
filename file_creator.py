import json
import util
from os import name, system, path

def make_json(directory):

    try:
        util.clear()

        iterations = int(input("How many entries do you want to make? (1-5) "))

        print(util.fcolor(6, util.header_c))

        for i in range(1, iterations+1):
            for j in range(0, 8):
                if j <= 2:
                    response = input(util.fields[j])
                    util.repos[i].update({util.keys[j]: response})
                elif j > 2 and j < 7:
                    response = float(input(util.fields[j]))
                    util.repos[i].update({util.keys[j]: response})
                elif j == 7:
                    old_bal = float(util.repos[i].get('old_bal'))
                    deposit = float(util.repos[i].get('deposit'))
                    withdraw = float(util.repos[i].get('withdraw'))

                    updated_bal = (old_bal + deposit) - withdraw
                    util.repos[i].update({util.keys[7]: updated_bal})

        statement1 = [{"info": util.repos[1]}]
        statement2 = [{"info": util.repos[2]}]
        statement3 = [{"info": util.repos[3]}]
        statement4 = [{"info": util.repos[4]}]
        statement5 = [{"info": util.repos[5]}]
        wrapper = {"statements": statement1 + statement2 +
                   statement3 + statement4 + statement5}

        print(util.fcolor(6, util.footer))

        file_name = input("current month & year>>")
        print(directory)

        completeName = path.join(
            directory, file_name + "_statement.json")

        print(util.fcolor(5, "Creating New File..."))

        with open(completeName, 'w') as json_file:
            json.dump(wrapper, json_file, indent=4, sort_keys=False)

        print(util.fcolor(2, "File Successfully Created!"))

        util.clear()

    except(Exception):
        print(util.fcolor(1, "Error creating JSON"))
        util.wait(2)
        util.clear()
