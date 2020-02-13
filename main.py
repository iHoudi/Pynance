import json
import os
import datetime

from mode_json import json_main, load_json

# requirements #
# 1. handle inputs for various expenditures... ex: csv, text
# 2. format these to json
# 3. Export the json formatted


class Pynance:

    def __init__(self):
        self.date = datetime.datetime.now().strftime("%D %H:%M")
        self.account_balance = 0
        self.deposit = 0
        self.withdraw = 0

    def main(self):

        while True:
            print("Mode selection:\n 0 = Load JSON,\n 1 = Load existing CSV file,\n 2 = input data to write to an initial JSON or CSV file")

            try:
                self.mode = int(input("Mode: "))
                if self.mode == 0:
                    json_main()
                elif self.mode == 1:
                    print("Loadiing existing CSV file")

                elif self.mode == 2:
                    self.account_balance = input(
                        "Please enter your initial account balance>> $")
                    print(f"Balance: ${self.account_balance}")

                else:
                    print("Issue loading data or invalid mode")
                return False

            except Exception:
                print(Exception)
                exit()


Pynance().main()
