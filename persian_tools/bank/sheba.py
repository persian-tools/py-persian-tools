from typing import Union
from .exceptions import InvalidShebaNumber
from .banks_code import data as banks_code


def _iso7064Mod97_10(iban: str) -> int:
    reminder = iban

    while len(reminder) > 2:
        block = reminder[:9]
        reminder = str(int(block) % 97) + reminder[len(block):]

    return int(reminder) % 97


def validate(sheba: str) -> bool:
    if len(sheba) != 26:
        return False

    if sheba[:2] != 'IR' or not sheba[2:].isdigit():
        return False

    d1 = ord(sheba[0]) - 65 + 10
    d2 = ord(sheba[1]) - 65 + 10

    new_code = sheba[4:] + str(d1) + str(d2) + sheba[2:4]
    reminder = _iso7064Mod97_10(new_code)

    return reminder == 1


def bank_data(sheba: str) -> Union[dict, None]:
    if not validate(sheba):
        raise InvalidShebaNumber(sheba)

    sheba_code = sheba[4:7]
    bank = [bank for bank in banks_code if sheba_code in bank.get('sheba_code', [])]

    if len(bank) < 1:
        return None

    data = bank[0].copy()
    if callable(data.get('account_number_calculator')):
        account_data = data['account_number_calculator'](sheba)
        data['account_number'] = account_data['normal']
        data['formatted_account_number'] = account_data['formatted']
        del data['account_number_calculator']
    return data
