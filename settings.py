from time import time_ns
import json
from typing import Dict, Optional
from datetime import datetime
from colorama import Fore
from services import print_error, print_info


def generate_id() -> str:
    return str(time_ns())


def generate_tm() -> str:
    return str(datetime.now())


def download_from_json(json_file) -> Optional[Dict[str, Dict[str, str]]]:
    """This function downloads the JSON file """
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print_error(f"File {json_file} not found.")
        return {}
    except json.JSONDecodeError:
        print_error(f"Could not decode JSON from {json_file}.")
        return {}


def download_to_json(data: dict) -> None:
    """This function downloads the dictionary to JSON file"""
    try:
        with open('db/users.json', 'w') as f:
            json.dump(data, f, indent=3)
    except Exception as e:
        print_error(f"An error occurred while writing to the file: {e}")


def to_find(what='full_name', attribute=None) -> Dict[str, str]:
    """This function checks if the attribute is in the database and return it"""
    data: dict = download_from_json('db/users.json')
    for user_id, user in data.items():
        if user[what].lower() == attribute.lower():
            return user


def choice_show() -> Optional[int]:
    print(Fore.LIGHTCYAN_EX + 'Here you can see users😊'
                              '\n1. To see all users\n2. To filter by full name\n0.Exit' + Fore.RESET)

    try:
        choice: int = int(input('\033[5;32;20m=='))
        if choice < 0 or choice > 2:
            print_error('Please enter a number between 0 and 2')
    except ValueError:
        print_error('Please enter a number')
    else:
        return choice


def choice_update() -> Optional[int]:
    """This function return choice to update the database"""
    print_info('What do you want to change:'
               '\n1. Change full name\n2. Change password'
               '\n3. Change phone number \n4. Change email'
               '\n5. Change language\n0. Exit')
    try:
        choice: int = int(input(Fore.BLACK + 'Enter your choice: ' + Fore.RESET))
        if choice < 0 or choice > 5:
            print_error('Please enter a number between 0 and 5')
    except ValueError:
        print_error('Invalid input. Please enter a number.')
    else:
        return choice


def choice_delete() -> Optional[int]:
    """This function return choice to delete users in the database"""
    while True:
        print_info('Welcome. Here you can delete users.\n0. Exit.\n1. Delete user.')
        try:
            choice: int = int(input('\033[6;30;20mEnter your choice: '))
            if choice > 1 or choice < 0:
                print_error('Please enter a number 0 or 1')
        except ValueError:
            print_error('Please enter a number 0 or 1')
        else:
            return choice
