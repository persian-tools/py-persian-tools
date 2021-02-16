from persian_tools import national_id
from persian_tools.national_id.exceptions import InvalidNationalId
import pytest


def test_validate_national_id():
    # this national id is equal to 0068415941
    assert national_id.validate('068415941')

    # this national id is equal to 0123000000
    assert national_id.validate('123000000') is False
    assert national_id.validate('0000000000') is False
    assert national_id.validate('4271427685') is False
    assert national_id.validate('0200203041') is False
    assert national_id.validate('0684159415') is False
    assert national_id.validate('068415941d') is False
    assert national_id.validate('06841594156') is False

    assert national_id.validate('0499370899')
    assert national_id.validate('0790419904')
    assert national_id.validate('0084575948')
    assert national_id.validate('0963695398')
    assert national_id.validate('0684159414')

    assert national_id.validate('0067749828')
    assert national_id.validate('0650451252')
    assert national_id.validate('1583250689')
    assert national_id.validate('4032152314')
    assert national_id.validate('0076229645')


def test_generate_random_national_id():
    for _ in range(15):
        assert national_id.validate(national_id.generate_random())


def test_find_place_national_id():
    assert national_id.find_place('0499370899').get('city') == 'شهرری'
    assert national_id.find_place('0790419904').get('city') == 'سبزوار'
    assert national_id.find_place('0084575948').get('city') == 'تهران مرکزی'
    assert national_id.find_place('0060495219').get('city') == 'تهران مرکزی'
    assert national_id.find_place('0671658506').get('city') == 'بجنورد'
    assert national_id.find_place('0671658506').get('city') == 'بجنورد'
    assert national_id.find_place('0643005846').get('city') == 'بیرجند'
    assert national_id.find_place('0906582709').get('city') == 'کاشمر'
    assert national_id.find_place('0451727304').get('city') == 'شمیران'
    assert national_id.find_place('0371359058').get('city') == 'قم'
    assert national_id.find_place('5049478618').get('city') == 'پارس آباد'
    assert national_id.find_place('2110990147').get('city') == 'گرگان'

    assert national_id.find_place('9982675801') is None

    with pytest.raises(InvalidNationalId, match='.*is an invalid national id'):
        national_id.find_place('0084545943')
        national_id.find_place('008454594')
        national_id.find_place('8881234567')
