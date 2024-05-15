import json

from typing import Dict, Optional, List
from colorama import Fore

from services import print_success
from view import user_show_pro, user_create_pro, user_update_pro, delete_user_pro


class Admin:
    logged_in_user = None

    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password

    @classmethod
    def download_to_json(cls, data: Dict[str, str]) -> None:
        with open('db/admins.json', 'w') as f:
            json.dump(data, f, indent=3)

    @classmethod
    def download_from_json(cls) -> List[Dict[str, str]]:
        with open('db/admins.json', 'r') as f:
            data = json.load(f)
            return data

    @classmethod
    def login(cls) -> bool:
        if cls.logged_in_user is not None:
            return True
        data = cls.download_from_json()
        username = input(Fore.LIGHTWHITE_EX + 'Enter your username please: ' + Fore.RESET)
        password = input(Fore.LIGHTWHITE_EX + 'Enter your password please: ' + Fore.RESET)
        for user in data:
            if user['name'].lower() == username.lower() and user['password'] == password:
                cls.logged_in_user = user
                return True
        return False

    @classmethod
    def menu(cls) -> Optional[str]:
        login = cls.login()
        while login:
            print(Fore.LIGHTYELLOW_EX + f'Welcome admin! Here you can: ' + Fore.RESET)

            return input(Fore.LIGHTCYAN_EX + f'1 => create user\n2 => delete user\n3 => update user'
                                             f'\n4 => read users\n0 => Exit'
                                             '\nYour choice .....' + Fore.RESET)

        else:
            raise Exception('Wrong password or username please try again')

    @classmethod
    def run(cls) -> None:
        while True:
            choice = cls.menu()
            if choice == '0':
                print(Fore.LIGHTCYAN_EX + 'The end of the program.'
                                          ' Thank you for using😊' + Fore.RESET)
                break
            elif choice == '1':
                user_create_pro()
            elif choice == '2':
                delete_user_pro()
            elif choice == '3':
                user_update_pro()
            elif choice == '4':
                user_show_pro()
            else:
                raise Exception('Wrong choice please enter number between 0 and 4')


class Teacher(Admin):
    logged_in_user: bool = None

    def __init__(self, name: str, password: str) -> None:
        super().__init__(name, password)

    @classmethod
    def download_from_json(cls) -> List[Dict[str, str]]:
        with open('db/teachers.json', 'r') as f:
            data: List[Dict[str, str]] = json.load(f)
            return data

    @classmethod
    def create_admin(cls) -> None:
        username: str = input(Fore.LIGHTWHITE_EX + 'Enter new admin\'s username: ' + Fore.RESET)
        password: str = input(Fore.LIGHTWHITE_EX + 'Enter new admin\'s password: ' + Fore.RESET)
        new_admin: Admin = Admin(username, password)
        data: List[Dict[str, str]] = Admin.download_from_json()
        for i, user in enumerate(data):
            if data[i]['name'].lower() == username.lower():
                raise ValueError(f'Username {username} already exists')
        data.append(new_admin.__dict__)
        Admin.download_to_json(data=data)
        print_success('Admin created successfully')

    @classmethod
    def delete_admin(cls) -> None:
        username: str = input(Fore.LIGHTWHITE_EX + 'Enter admin\'s username to delete: ' + Fore.RESET)
        password: str = input(Fore.LIGHTWHITE_EX + 'Enter admin\'s password to delete: ' + Fore.RESET)
        data: List[Dict[str, str]] = Admin.download_from_json()
        for i, user in enumerate(data, start=0):
            if data[i]['name'].lower() == username.lower() and data[i]['password'] == password:
                del data[i]
                Admin.download_to_json(data=data)
                print_success('Admin deleted successfully')

        raise ValueError(f'Wrong password or username of admin')

    @classmethod
    def update_admin(cls) -> None:
        username: str = input('Enter username : ')
        password: str = input('Enter password : ')
        data: List[Dict[str, str]] = Admin.download_from_json()
        for i, user in enumerate(data, start=0):
            if data[i]['name'].lower() == username.lower() and data[i]['password'] == password:
                print(Fore.LIGHTYELLOW_EX + 'What do you want to change:' + Fore.RESET)
                choice = input(Fore.LIGHTCYAN_EX + '1. Username\n2. Password\n0 Exit\n...' + Fore.RESET)
                if choice == '1':
                    new_username = input('Enter new username : ')
                    data[i]['name'] = new_username
                    Admin.download_to_json(data=data)
                    print_success('Successfully updated')
                elif choice == '2':
                    new_password = input('Enter new password : ')
                    data[i]['password'] = new_password
                    Admin.download_to_json(data=data)
                    print_success('Successfully updated')
                elif choice == '0':
                    break
                return
        raise ValueError(f'Wrong enter, please enter number between 0 and 2 ')

    @classmethod
    def show_admin(cls) -> None:
        data: List[Dict[str, str]] = Admin.download_from_json()
        print(json.dumps(data, indent=4, sort_keys=True))

    @classmethod
    def login(cls) -> bool:
        if cls.logged_in_user is not None:
            return True

        data: List[Dict[str, str]] = cls.download_from_json()
        username: str = input(Fore.LIGHTWHITE_EX + 'Enter your username please: ' + Fore.RESET)
        password: str = input(Fore.LIGHTWHITE_EX + 'Enter your password please: ' + Fore.RESET)
        for user in data:
            if user['name'].lower() == username.lower() and user['password'] == password:
                cls.logged_in_user = user
                return True
        return False

    @classmethod
    def menu(cls) -> Optional[str]:
        login: bool = cls.login()
        if login:
            print(Fore.LIGHTYELLOW_EX + 'Welcome teacher! Here you can: ' + Fore.RESET)
            return input(Fore.LIGHTCYAN_EX + '1 => create admin\n2 => delete admin\n3 => update admin'
                                             '\n4 => show admin\n\n0 => Exit'
                                             '\nYour choice .....' + Fore.RESET)
        else:
            raise Exception('Wrong password or username please try again')

    @classmethod
    def run(cls) -> None:
        while True:
            choice = cls.menu()
            if choice == '1':
                cls.create_admin()
            elif choice == '2':
                cls.delete_admin()
            elif choice == '3':
                cls.update_admin()
            elif choice == '4':
                cls.show_admin()
            elif choice == '0':
                print_success('Thank you for using')
                break
            else:
                raise Exception('Wrong choice please enter number between 0 and 4')


class Guest:

    @classmethod
    def menu(cls) -> Optional[str]:
        return input(Fore.LIGHTMAGENTA_EX + "Welcome Guest. Here you can: "
                                            '\n1 => Show users\n2 => Create users'
                                            '\n0 => Exit \nYour choice....' + Fore.RESET)

    @classmethod
    def run(cls) -> None:
        while True:
            choice = cls.menu()
            if choice == '1':
                user_show_pro()
            elif choice == '2':
                user_create_pro()
            elif choice == '0':
                break
            else:
                raise Exception('Invalid choice, please enter number between 0 and 2')
