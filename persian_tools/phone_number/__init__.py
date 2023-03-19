import re
from typing import Union
from .operators import data as operators_data
from .exceptions import InvalidPhoneNumber, InvalidToken

MOBILE_REGEX = '(?:[+|0{2}]?98)?(?:0)?(\\d{3})+(\\d{3})+(\\d{4})'
VALID_TOKENS = ['+98', '98', '0098', '0']
MOBILE_SUFFIX_REGEX = '^(?:\+98|98|0098|0)'


def _get_operator_data(phone_number: str) -> Union[dict, bool]:
    phone_number_suffix = re.split(MOBILE_SUFFIX_REGEX, phone_number).pop()
    for prefix_length in range(3, 6):
        operator_prefix = phone_number_suffix[:prefix_length]
        if operators_data.get(operator_prefix):
            return operators_data.get(operator_prefix)

    return False


def validate(phone_number: str) -> bool:
    return _get_operator_data(phone_number) is not False


def operator_data(phone_number: str) -> bool:
    res = _get_operator_data(phone_number)
    if res is False:
        raise InvalidPhoneNumber(phone_number)

    return res


def normalize(phone_number: str, token: str = '0') -> str:
    if token not in VALID_TOKENS:
        raise InvalidToken(token)

    valid = validate(phone_number)
    if valid is False:
        raise InvalidPhoneNumber(phone_number)

    phone_number_suffix = re.split(MOBILE_SUFFIX_REGEX, phone_number).pop()
    return token + phone_number_suffix
