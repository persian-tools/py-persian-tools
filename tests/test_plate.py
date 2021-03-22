from persian_tools import plate
from persian_tools.plate.exceptions import InvalidPlateLength
import pytest


def test_plate_type():
    assert plate.get_info('12ب14547').get('type') == plate.TYPE_CAR
    assert plate.get_info('12ب145478').get('type') == plate.TYPE_MOTORCYCLE

    with pytest.raises(InvalidPlateLength, match='.*digits long, must be 7 or 8'):
        plate.get_info('12ب1454789').get('type')


def test_car_plate_info():
    actual = plate.get_info('12ب14547')
    expected = {
        'type': plate.TYPE_CAR,
        'template': '12ب145ایران47',
        'province': 'مرکزی',
        'category': 'شخصی'
    }
    assert all(v == actual[k] for k, v in expected.items())
    assert len(expected) == len(actual)

    actual = plate.get_info('12ب14547')
    assert all(v == actual[k] for k, v in expected.items())
    assert len(expected) == len(actual)

    actual = plate.get_info('1214501')
    expected = {
        'type': plate.TYPE_CAR,
        'template': '12None145ایران1',
        'province': None,
        'category': None
    }
    assert all(v == actual[k] for k, v in expected.items())
    assert len(expected) == len(actual)


def test_motorcycle_plate_info():
    actual = plate.get_info('12145478')
    expected = {
        'type': plate.TYPE_MOTORCYCLE,
        'template': '121-45478',
        'province': 'مرکز تهران',
        'category': None
    }
    assert all(v == actual[k] for k, v in expected.items())
    assert len(expected) == len(actual)

    actual = plate.get_info('10045118')
    expected = {
        'type': plate.TYPE_MOTORCYCLE,
        'template': '100-45118',
        'province': None,
        'category': None
    }
    assert all(v == actual[k] for k, v in expected.items())
    assert len(expected) == len(actual)


def test_is_valid_function():
    assert plate.is_valid('12ب14547')  # valid car plate
    assert plate.is_valid('12145478')  # valid motorcycle plate
    assert plate.is_valid('12ب145774347') is False  # long plate number, for car plate
    assert plate.is_valid('121454789') is False  # long plate number, for motorcycle plate
    assert plate.is_valid('1214501') is False  # fake province code (01), for car plate
    assert plate.is_valid('10045118') is False  # fake province code (100), for motorcycle plate
    assert plate.is_valid('12g45147') is False  # invalid car plate character
    assert plate.is_valid('12الف45150') is False  # fake province code (50), for car plate
    assert plate.is_valid('10045678') is False  # fake province code (100), for motorcycle plate
    assert plate.is_valid('10045678') is False  # fake province code (100), for motorcycle plate

    assert plate.is_valid('12345678')
    assert plate.is_valid('12345670')
    assert plate.is_valid('1230567') is False
    assert plate.is_valid('12305678') is False
    assert plate.is_valid('1ی23456') is False
    assert plate.is_valid('1234f560') is False
    assert plate.is_valid('123450d0') is False


def test_normalize():
    actual = plate.normalize('1234567الف')
    expected = {
        'numbers': '1234567',
        'char': 'الف',
    }
    assert all(v == actual[k] for k, v in expected.items())
    assert len(expected) == len(actual)

    actual = plate.normalize('1234567')
    expected = {
        'numbers': '1234567',
        'char': None,
    }
    assert all(v == actual[k] for k, v in expected.items())
    assert len(expected) == len(actual)
