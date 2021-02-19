from persian_tools.bank import card_number
from persian_tools.bank.exceptions import InvalidCardNumber
import pytest


def test_validate():
    assert card_number.validate('6037701689095443')
    assert card_number.validate('6219861034529007')
    assert card_number.validate('6219861034529008') is False
    assert card_number.validate('621986103452900') is False
    assert card_number.validate('0') is False


def test_bank_name():
    assert card_number.bank_name('6037701689095443') == 'بانک کشاورزی'
    assert card_number.bank_name('6219861034529007') == 'بانک سامان'
    assert card_number.bank_name('6219861034529007') == 'بانک سامان'

    assert card_number.bank_name('1319861034529007') is None

    with pytest.raises(InvalidCardNumber, match='.*is an invalid card number'):
        card_number.bank_name('621986103452900')
        card_number.bank_name('9999991034529007')


mock_string = '''شماره کارتم رو برات نوشتم:
    6219-8610-3452-9007
    اینم یه شماره کارت دیگه ای که دارم
    5022291070873466
    ۵۰۲۲۲۹۱۰۸۱۸۷۳۴۶۶
    ۵۰۲۲-۲۹۱۰-۷۰۸۷-۳۴۶۶'''


def test_extract_card_numbers_1():
    """Should find and extract 4 Card Numbers"""

    expected = [
        {'pure': '6219861034529007', 'base': '6219-8610-3452-9007', 'index': 1},
        {'pure': '5022291070873466', 'base': '5022291070873466', 'index': 2},
        {'pure': '5022291081873466', 'base': '۵۰۲۲۲۹۱۰۸۱۸۷۳۴۶۶', 'index': 3},
        {'pure': '5022291070873466', 'base': '۵۰۲۲-۲۹۱۰-۷۰۸۷-۳۴۶۶', 'index': 4},
    ]
    actual = card_number.extract_card_numbers(mock_string, check_validation=False)

    assert len(actual) == 4
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])


def test_extract_card_numbers_2():
    """Should find and format the Card-Number into Text that includes Persian & English digits"""
    mock_string_2 = '''شماره کارتم رو برات نوشتم: ۵۰۲۲-2910-7۰۸۷-۳۴۶۶'''

    expected = [
        {'pure': '5022291070873466', 'base': '۵۰۲۲-2910-7۰۸۷-۳۴۶۶', 'index': 1},
    ]
    actual = card_number.extract_card_numbers(mock_string_2, check_validation=False)

    assert len(actual) == 1
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])


def test_extract_card_numbers_3():
    """Should validate extract card-numbers"""

    expected = [
        {'pure': '6219861034529007', 'base': '6219-8610-3452-9007', 'index': 1, 'is_valid': True},
        {'pure': '5022291070873466', 'base': '5022291070873466', 'index': 2, 'is_valid': True},
        {'pure': '5022291081873466', 'base': '۵۰۲۲۲۹۱۰۸۱۸۷۳۴۶۶', 'index': 3, 'is_valid': False},
        {'pure': '5022291070873466', 'base': '۵۰۲۲-۲۹۱۰-۷۰۸۷-۳۴۶۶', 'index': 4, 'is_valid': True},
    ]
    actual = card_number.extract_card_numbers(mock_string, check_validation=True, filter_valid_card_numbers=False)

    assert len(actual) == 4
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])


def test_extract_card_numbers_4():
    """Should return only valid card-numbers"""

    expected = [
        {'pure': '6219861034529007', 'base': '6219-8610-3452-9007', 'index': 1, 'is_valid': True},
        {'pure': '5022291070873466', 'base': '5022291070873466', 'index': 2, 'is_valid': True},
        {'pure': '5022291070873466', 'base': '۵۰۲۲-۲۹۱۰-۷۰۸۷-۳۴۶۶', 'index': 4, 'is_valid': True},
    ]
    actual = card_number.extract_card_numbers(mock_string, check_validation=True, filter_valid_card_numbers=True)

    assert len(actual) == 3
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])

    actual_without_attr = card_number.extract_card_numbers(mock_string)

    assert len(actual) == len(actual_without_attr)
    assert all([a == b for a, b in zip(actual, actual_without_attr)])


def test_extract_card_numbers_5():
    """Should detect Banks number for valid card-numbers"""

    expected = [
        {'pure': '6219861034529007', 'base': '6219-8610-3452-9007', 'index': 1, 'is_valid': True,
         'bank_name': 'بانک سامان'},
        {'pure': '5022291070873466', 'base': '5022291070873466', 'index': 2, 'is_valid': True,
         'bank_name': 'بانک پاسارگاد'},
        {'pure': '5022291070873466', 'base': '۵۰۲۲-۲۹۱۰-۷۰۸۷-۳۴۶۶', 'index': 4, 'is_valid': True,
         'bank_name': 'بانک پاسارگاد'},
    ]

    actual = card_number.extract_card_numbers(mock_string, check_validation=True, filter_valid_card_numbers=True,
                                              detect_bank_name=True)

    assert len(actual) == 3
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])
