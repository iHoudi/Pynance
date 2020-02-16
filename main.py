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

        # Keeps track of how many times input has been provided. IF it reaches '2' the program will exit
        n = 0

        # Provides the loop for the program
        while True:
            # Attempts to take user input and call the appropriate method
            try:
                print(
                    "Mode selection:\n 0 = load existing file,\n 1 = Create new file,\n 2 = Exit out of Pynance")
                self.mode = int(input("Mode: "))

                if self.mode == 0:
                    file_selector()

                elif self.mode == 1:
                    make_json()

                elif self.mode == 2:
                    exit()

                elif n == 2:
                    # We do 'n+1' to display the amount of invalid entries with a base of '1' instead of '0'
                    print(f"{n+1} invalid entries... Exiting program.")
                    exit()

                else:
                    print("Mode not listed\n")
                    n += 1

            except(ValueError):
                if n == 2:
                    # Refer to the comment on line 38
                    print(f"{n+1} invalid entries... Exiting program.")
                    exit()

                n += 1
                print("Invalid Input\n")


Pynance().main()
