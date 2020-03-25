import util
import displayer
from colorama import init


def run():
    while True:
        init(autoreset=True)

        _return = util.return_check()
        if _return != 1:
            #print("Pre_init_Menu")
            displayer.display(_return)

        else:
            #print("Post_init_Menu")
            displayer.display(_return)


if __name__ == '__main__':
    #print(util.getOS())
    run()
