import json
import os

from import_handler import file_selector, mode_json
from file_creator import make_json

# requirements #
# 1. handle inputs for various expenditures... ex: csv, text
# 2. format these to json
# 3. Export the json formatted


class Pynance:

    def main(self):

        while True:
            print(
                "Mode selection:\n 0 = load existing file,\n 1 = Create new file,\n 2 = Exit out of Pynance")

            self.mode = int(input("Mode: "))
            if self.mode == 0:
                file_selector()
            elif self.mode == 1:
                make_json()
            elif self.mode == 2:
                exit()
            else:
                print("Issue loading data or invalid mode")
            return False


Pynance().main()
