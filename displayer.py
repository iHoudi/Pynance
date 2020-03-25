import file_creator
import import_handler
import util


def display(int):

    print(util.header)
    if int != 0:
        for option in range(0, int+2):
            print(util.menu_options[option])
    else:
        for option in range(1, int+3):
            print(util.menu_options[option])
    print(util.footer)

    user_in = input('>>', ).upper()

    if user_in == 'C':
        file_creator.make_json(util.get_file_path())
    elif user_in == 'L':
        import_handler.load_json()
    elif user_in == 'E':
        util.clear()
        exit()
    else:
        print("Invalid input! Try Again")
        util.wait(1)
        util.clear()
