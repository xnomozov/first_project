import time
from typing import Optional

from colorama import Fore
import bcrypt


def print_error(message: str) -> None:
    print(Fore.LIGHTRED_EX + message + Fore.RESET)


def print_info(message: str) -> None:
    print(Fore.LIGHTCYAN_EX + message + Fore.RESET)


def print_success(message: str) -> None:
    print(Fore.LIGHTGREEN_EX + message + Fore.RESET)


def menu() -> Optional[int]:
    """This function allows users to choose an option"""

    print_info('1 ---> Login as Guest.\n2 ---> Login as Admin.\n3 ---> Login as Teacher.'
               '\n0 ---> To quit')

    while True:
        try:
            choice = int(input(Fore.LIGHTWHITE_EX + 'Your choice => ' + Fore.RESET))
            if 0 <= choice <= 4:
                return choice
            else:
                print_error('Please enter a number between 0 and 4')
        except ValueError:
            print_error('Please enter a number between 0 and 4')


def encode_password(raw_password: str) -> bcrypt.hashpw:
    encoded_password = raw_password.encode('utf-8')
    salt = bcrypt.gensalt(4)
    return bcrypt.hashpw(encoded_password, salt)
