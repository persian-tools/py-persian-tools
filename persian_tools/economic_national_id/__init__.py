import random


def validate(economic_national_id: str) -> bool:
    """Validate the given economic national ID.

    Args:
        economic_national_id (str): A 11-length numerical string.

    Returns:
        bool: True if the ID is valid, otherwise False.
    """    
    coef = [29, 27, 23, 19, 17]
    code = economic_national_id.zfill(11)

    if not code.isdigit() or len(code) != 11:
        return False

    _constant = int(code[-2]) + 2
    _sum = 0
    for i in range(10):
        _sum += (int(code[i]) + int(_constant)) * coef[i % 5]

    remainder = 0 if _sum % 11 == 10 else _sum % 11

    return remainder == int(code[-1])


def generate_random() -> str:
    """Generate valid Economic National ID according the released validation algorithms.

    Returns:
        str: A valid economic national ID.
    """    
    coef = [29, 27, 23, 19, 17]

    while True:
        counter += 1
        random_number = random.randint(10 ** 9, 10 ** 10 - 1)
        random_number = str(random_number).zfill(10)

        _constant = int(random_number[-2]) + 2
        _sum = 0
        for i in range(10):
            _sum += (int(random_number[i]) + int(_constant)) * coef[i % 5]

        last_number = 0 if _sum % 11 == 10 else _sum % 11
        if validate(random_number + str(last_number)):
            break

    return random_number + str(last_number)
