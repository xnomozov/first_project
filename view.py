from typing import Dict

from colorama import Fore

from dao import create_user, show_user, update_user, delete_user
from errors import BadRequestError
from htttp import Response
from model import User
from services import print_error
from settings import generate_id, download_to_json, download_from_json, to_find
from validators import check_validators


def user_create_pro() -> Response:
    try:
        """This function creates new user, and downloads it to JSON file"""
        data: Dict[str, Dict[str, str]] = download_from_json('db/users.json')
        full_name: str = input('\033[6;30;20mEnter full name: ').title()
        user1: Dict[str, str] = to_find(attribute=full_name)
        if user1:
            print_error('Username already exists')
        else:
            user_id: str = generate_id()
            new_user: User = create_user()
            new_user.full_name = full_name
            new_user.user_id = user_id
            check_validators(new_user)
            data[user_id] = new_user.__dict__
            download_to_json(data=data)
            return Response(Fore.GREEN + 'Successfully created', status_code=202)
    except BadRequestError:
        return Response(Fore.RED + 'Bad requests', status_code=404)


def user_show_pro() -> None:
    """This function shows user's attributes"""
    show_user()


def user_update_pro() -> Response:
    """This function updates user's attributes"""
    update = update_user()
    if update:
        return Response(Fore.GREEN + 'Successfully updated', status_code=202)
    else:
        return Response(Fore.RED + 'Bad requests', status_code=404)


def delete_user_pro() -> Response:
    """This function deletes user's attributes"""
    delete = delete_user()
    if delete:
        return Response(Fore.GREEN + 'Successfully deleted', status_code=202)
    else:
        return Response(Fore.RED + 'Bad requests', status_code=404)
