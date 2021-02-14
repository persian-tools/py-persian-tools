from typing import Union
import random


def verify(national_id: Union[int, str]) -> bool:
    code = str(national_id).zfill(10)

    if not code.isdigit() or len(code) != 10:
        return False

    if int(code[3:-1]) == 0:
        return False

    _sum = 0
    for i in range(9):
        _sum += int(code[i]) * (10 - i)

    remaining = _sum % 11
    check_number = int(code[-1])

    if remaining < 2:
        return check_number == remaining
    return check_number == 11 - remaining


def generate_random() -> str:
    random_number = random.randint(10 ** 6, 10 ** 9 - 1)
    random_number = str(random_number).zfill(9)

    _sum = 0
    for i in range(9):
        _sum += int(random_number[i]) * (10 - i)

    remaining = _sum % 11
    if remaining < 2:
        last_number = remaining
    else:
        last_number = 11 - remaining

    return random_number + str(last_number)
