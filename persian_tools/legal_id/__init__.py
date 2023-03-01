import random

_COEFFICIENT = [29, 27, 23, 19, 17]


def validate(legal_id: str) -> bool:
    code = legal_id.zfill(11)

    if not code.isdigit() or len(code) != 11:
        return False

    _constant = int(code[-2]) + 2
    _sum = 0
    for i in range(10):
        _sum += (int(code[i]) + int(_constant)) * _COEFFICIENT[i % 5]

    remainder = 0 if _sum % 11 == 10 else _sum % 11

    return remainder == int(code[-1])


def generate_random() -> str:
    random_number = random.randint(10 ** 8, 10 ** 10 - 1)
    random_number = str(random_number).zfill(10)

    _constant = int(random_number[-1]) + 2
    _sum = 0
    for i in range(10):
        _sum += (int(random_number[i]) + int(_constant)) * _COEFFICIENT[i % 5]

    remainder = _sum % 11
    if _sum % 11 == 10:
        remainder = 0

    return random_number + str(remainder)
