from model import User
from errors import BadRequestError


def check_validators(user: User) -> None:
    if not user.phone_number:
        raise BadRequestError('Phone number is not None')

    if not user.password:
        raise BadRequestError('Password is not None')

