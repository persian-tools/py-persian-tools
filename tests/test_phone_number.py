from persian_tools import phone_number
from persian_tools.phone_number.exceptions import InvalidPhoneNumber, InvalidToken
import pytest


def test_validate():
    assert phone_number.validate('09022002580')
    assert phone_number.validate('09122002580')
    assert phone_number.validate('09322002580')
    assert phone_number.validate('09192002580')
    assert phone_number.validate('+989022002580')
    assert phone_number.validate('09022002580')
    assert phone_number.validate('989022002580')
    assert phone_number.validate('00989022002580')
    assert phone_number.validate('9022002580')

    assert phone_number.validate('09802002580') is False
    assert phone_number.validate('0980200') is False


def test_operator_data():
    actual = phone_number.operator_data('09022002580')
    expected = {'province': [], 'base': 'کشوری', 'type': ['permanent', 'credit'],'operator': 'ایرانسل'}
    assert all(v == actual[k] for k, v in expected.items())
    assert len(expected) == len(actual)

    actual = phone_number.operator_data('09981000000')
    expected = {'province': [], 'base': 'کشوری', 'type': ['credit'], 'operator': 'شاتل موبایل'}
    assert all(v == actual[k] for k, v in expected.items())
    assert len(expected) == len(actual)

    actual = phone_number.operator_data('09300880440')
    expected = {'province': [], 'base': 'کشوری', 'type': ['permanent', 'credit'], 'operator': 'ایرانسل'}
    assert all(v == actual[k] for k, v in expected.items())
    assert len(expected) == len(actual)

    actual = phone_number.operator_data('09999980440')
    expected = {'province': [], 'base': 'کشوری', 'type': ['credit', 'permanent'], 'operator': 'سامانتل'}
    assert all(v == actual[k] for k, v in expected.items())
    assert len(expected) == len(actual)

    with pytest.raises(InvalidPhoneNumber, match='.*is an invalid phone number'):
        phone_number.operator_data('+989990467927')


def test_normalize():
    assert phone_number.normalize('+989373708555', '0') == '09373708555'
    assert phone_number.normalize('989373708555', '0') == '09373708555'
    assert phone_number.normalize('00989022002580', '0') == '09022002580'
    assert phone_number.normalize('09122002580', '0') == '09122002580'
    assert phone_number.normalize('9322002580', '0') == '09322002580'

    assert phone_number.normalize('09373708555', '+98') == '+989373708555'
    assert phone_number.normalize('09022002580', '+98') == '+989022002580'
    assert phone_number.normalize('09122002580', '+98') == '+989122002580'
    assert phone_number.normalize('9322002580', '+98') == '+989322002580'
    assert phone_number.normalize('00989022002580', '+98') == '+989022002580'

    assert phone_number.normalize('9322002580', '+98') == '+989322002580'
    assert phone_number.normalize('9322002580', '98') == '989322002580'
    assert phone_number.normalize('9322002580', '0098') == '00989322002580'
    assert phone_number.normalize('9322002580', '0') == '09322002580'
    assert phone_number.normalize('9322002580') == '09322002580'

    with pytest.raises(InvalidPhoneNumber, match='.*is an invalid phone number'):
        phone_number.normalize('0', '+98')
        phone_number.normalize('+98', '+98')
        phone_number.normalize('99999999999', '+98')
        phone_number.normalize('   99999999     ', '+98')
        phone_number.normalize('09802002580', '0')

    with pytest.raises(InvalidToken, match='.*is an invalid token'):
        phone_number.normalize('9322002580', '098')
