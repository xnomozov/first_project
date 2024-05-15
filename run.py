import time

from colorama import Fore

from services import menu
from users import Admin, Teacher, Guest


def run() -> None:
    """This function runs all the functions"""
    while True:
        choice: int = menu()
        if choice == 0:
            print(Fore.LIGHTCYAN_EX + 'The end of the program.'
                                      ' Thank you for using😊' + Fore.RESET)

            break
        elif choice == 1:
            Guest.run()
        elif choice == 2:
            Admin.run()
        elif choice == 3:
            Teacher.run()


if __name__ == '__main__':
    run()
