from persian_tools.bank import sheba
from persian_tools.bank.exceptions import InvalidShebaNumber
import pytest


def test_validate():
    assert sheba.validate('IR820540102680020817909002')
    assert sheba.validate('IR550570022080013447370101')

    assert sheba.validate('IR01234567890123456789') is False
    assert sheba.validate('IR012345678901234567890123456789') is False
    assert sheba.validate('IR01234567890123456789') is False
    assert sheba.validate('IR012345678901234567890123') is False
    assert sheba.validate('IR012345678901234567890123') is False
    assert sheba.validate('01234567890123456789012345') is False


def test_bank_data():
    actual = sheba.bank_data('IR820540102680020817909002')
    expected = {
        'nickname': 'parsian',
        'name': 'Parsian Bank',
        'persian_name': 'بانک پارسیان',
        'card_prefix': ['622106', '627884'],
        'sheba_code': ['054'],
        'account_number': '020817909002',
        'formatted_account_number': '002-00817909-002'
    }
    assert all(v == actual[k] for k, v in expected.items())
    assert len(expected) == len(actual)

    actual = sheba.bank_data('IR550570022080013447370101')
    expected = {
        'nickname': 'pasargad',
        'name': 'Pasargad Bank',
        'persian_name': 'بانک پاسارگاد',
        'card_prefix': ['502229', '639347'],
        'sheba_code': ['057'],
        'account_number': '220800134473701',
        'formatted_account_number': '220-800-13447370-1'
    }
    assert all(v == actual[k] for k, v in expected.items())
    assert len(expected) == len(actual)

    actual = sheba.bank_data('IR790610000000700796858044')
    expected = {
        'nickname': 'shahr',
        'name': 'City Bank',
        'persian_name': 'بانک شهر',
        'card_prefix': ['502806', '504706'],
        'sheba_code': ['061'],
        'account_number': '700796858044',
        'formatted_account_number': '700796858044'
    }
    assert all(v == actual[k] for k, v in expected.items())
    assert len(expected) == len(actual)

    with pytest.raises(InvalidShebaNumber, match='.*is an invalid sheba number'):
        sheba.bank_data('IR012345678901234567890123')
        sheba.bank_data('IR012345678A01234567890123')
