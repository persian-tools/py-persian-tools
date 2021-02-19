import re
from typing import Union
from ..exceptions import InvalidCardNumber
from .banks_code import data as banks_code
from ...digits import convert_to_en


def validate(card_number: str) -> bool:
    if not card_number.isdigit() or \
            len(card_number) != 16 or \
            int(card_number[1:10]) == 0 or \
            int(card_number[10:]) == 0:
        return False

    _sum = 0
    for i in range(16):
        ratio = 2 if i % 2 == 0 else 1
        res = int(card_number[i]) * ratio
        _sum += res - 9 if res > 9 else res

    return _sum % 10 == 0


def bank_name(card_number: str) -> Union[str, None]:
    if not validate(card_number):
        raise InvalidCardNumber(card_number)

    bank_code = card_number[:6]
    bank_names = [bank['name'] for bank in banks_code if bank['code'] == bank_code]

    if bank_names:
        return bank_names[0]
    return None


def extract_card_numbers(text: str, check_validation: bool = True, detect_bank_name: bool = False,
                         filter_valid_card_numbers: bool = True):
    card_number_regex = r'([\u06F0-\u06F90-9-_.*]{16,20})'
    results = []

    for i, matched_card_number in enumerate(re.findall(card_number_regex, text, re.MULTILINE)):
        card_number = convert_to_en(matched_card_number)

        for sep in ['-', '_', '.', '*']:
            if sep in matched_card_number:
                card_number = card_number.replace(sep, '')

        result = {
            'index': i + 1,
            'base': matched_card_number,
            'pure': card_number
        }

        if check_validation:
            result['is_valid'] = validate(card_number)

        if detect_bank_name and (result.get('is_valid') or validate(card_number)):
            result['bank_name'] = bank_name(card_number)

        results.append(result)

    if filter_valid_card_numbers and check_validation:
        results = [res for res in results if res['is_valid']]

    return results
