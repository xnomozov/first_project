from datetime import datetime
from typing import Dict

from enums import en
from model import User
from settings import (download_from_json, download_to_json,
                      to_find, choice_show, choice_update,
                      generate_tm, choice_delete)
from colorama import Fore
from services import print_error, print_info, print_success,encode_password
import json


def create_user() -> User:
    """This function create a new user"""
    phone_number: str = input(Fore.BLACK + 'Enter phone number: ' + Fore.RESET)
    email: str = input(Fore.BLACK + 'Enter email: ' + Fore.RESET)
    created_at = str(datetime.now())
    language: str = en
    password: str = input(Fore.BLACK + 'Enter password: ' + Fore.RESET)
    new_user: User = User(
        password=str(encode_password(password)), created_at=created_at,
        language=language,
        email=email, phone_number=phone_number)
    return new_user


def show_user() ->None:
    """This function show all users without id"""
    data: Dict[str, Dict[str, str]] = download_from_json('db/users.json')
    while True:
        choice: int = choice_show()
        if choice == 0:
            break
        elif choice == 1:
            print(json.dumps(data, indent=4))
        elif choice == 2:
            full_name: str = input(Fore.LIGHTBLACK_EX + 'Enter full name : ' + Fore.RESET)
            user = to_find('full_name', full_name)
            if user:
                print(json.dumps(user, indent=4))
            else:
                print_error('User not found')


def update_user() -> None:
    """This function updates user information and saves it to the JSON file."""
    data: Dict[str, Dict[str, str]] = download_from_json('db/users.json')
    if data:
        full_name: str = input(Fore.BLACK + 'Enter full name which you want to change: ' + Fore.RESET).title()
        user_id = None
        for key, value in data.items():
            if value['full_name'].lower() == full_name.lower():
                user_id = key
                break
        if user_id is None:
            return False
        else:
            while True:
                choice: int = choice_update()
                if choice == 0:
                    print_error('Exiting update mode.')
                    break

                elif 1 <= choice <= 5:
                    # add time when last time updated user
                    data[user_id]['updated_at'] = generate_tm()
                    attribute_keys: list = list(data[user_id].keys())
                    new_value: str = input(Fore.BLACK + f'Enter new {attribute_keys[choice - 1]}: ' + Fore.RESET)
                    data[user_id][attribute_keys[choice - 1]] = new_value
                    download_to_json(data=data)
                    return True

        return False


def delete_user() -> None:
    """This function deletes user information and saves it to the JSON"""
    data: Dict[str, Dict[str, str]] = download_from_json('db/users.json')
    if data:
        while True:
            choice = choice_delete()
            if choice == 0:
                print_info('End deleting')
                break
            elif choice == 1:
                username: str = input(Fore.BLACK + 'Enter username to delete: ' + Fore.RESET)
                user = to_find(attribute=username)
                if user:
                    password: str = input(Fore.BLACK + 'Enter password to delete: ' + Fore.RESET).lower()
                    user = to_find('password', password)
                    if user:
                        for user_id in data:
                            if data[user_id] == user:
                                try:
                                    choice = int(
                                        input(Fore.LIGHTWHITE_EX + 'Are you really sure you want to delete this user? '
                                                                   '\nyes => 1 \nno => 2\n.... ' + Fore.RESET))
                                except ValueError:
                                    return False
                                if choice == 1:
                                    del data[user_id]
                                    download_to_json(data=data)
                                    return True
                                else:
                                    print_success('User isn\'t deleted')
                    else:
                        return False
                else:
                    return False
