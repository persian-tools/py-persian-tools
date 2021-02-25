import re
from typing import Union
from .operators import data as operators_data
from .exceptions import InvalidPhoneNumber

MOBILE_REGEX = '(?:[+|0{2}]?98)?(?:0)?(\\d{3})+(\\d{3})+(\\d{4})'


def _get_operator_data(phone_number: str) -> Union[dict, bool]:
    found_number = re.findall(MOBILE_REGEX, phone_number)
    if found_number:
        prefix = found_number[0][0]
        return operators_data.get(prefix, False)

    return False


def validate(phone_number: str) -> bool:
    return _get_operator_data(phone_number) is not False


def operator_data(phone_number: str) -> bool:
    res = _get_operator_data(phone_number)

    if res is False:
        raise InvalidPhoneNumber(phone_number)

    return res
