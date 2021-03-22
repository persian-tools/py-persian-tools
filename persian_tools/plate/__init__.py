import re
from .dataset import provinces as plate_provinces, categories as plate_categories
from .dataset import TYPE_CAR, TYPE_MOTORCYCLE
from .exceptions import InvalidPlateLength


def normalize(plate: str):
    non_digit_regex = r'\D'
    char = ''.join(re.findall(non_digit_regex, plate)) or None
    numbers = re.sub(non_digit_regex, '', plate)
    return {'char': char, 'numbers': numbers}


def _car_info(char: str, numbers: str):
    province_code = int(numbers[5:7])
    _type = TYPE_CAR
    template = numbers[0:2] + str(char) + numbers[2:5] + 'ایران' + str(province_code)

    province = plate_provinces[_type].get(province_code)
    category = plate_categories.get(char)

    return {
        'type': _type,
        'template': template,
        'province': province,
        'category': category
    }


def _motorcycle_info(numbers: str):
    province_code = int(numbers[0:3])
    _type = TYPE_MOTORCYCLE
    template = str(province_code) + '-' + numbers[3:]

    province = plate_provinces[_type].get(province_code)

    return {
        'type': _type,
        'template': template,
        'province': province,
        'category': None
    }


def get_info(plate: str):
    normal_plate = normalize(plate)

    if len(normal_plate['numbers']) == 7:
        return _car_info(normal_plate['char'], normal_plate['numbers'])

    if len(normal_plate['numbers']) == 8:
        return _motorcycle_info(normal_plate['numbers'])

    raise InvalidPlateLength(plate)


def is_valid(plate: str):
    normal_plate = normalize(plate)
    numbers = normal_plate['numbers']

    for num in numbers[:-1]:
        if num == '0':
            return False

    if len(numbers) < 7 or len(numbers) > 8:
        return False

    info = get_info(plate)
    if info.get('type') == TYPE_CAR and info.get('category') is None:
        return False

    if info.get('province') is None:
        return False

    return True
