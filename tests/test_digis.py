from persian_tools import digits


def test_convert_to_fa():
    assert digits.convert_to_fa('123٤٥٦') == '۱۲۳۴۵۶'
    assert digits.convert_to_fa(123456) == '۱۲۳۴۵۶'


def test_convert_to_ar():
    assert digits.convert_to_ar('123۴۵۶') == '١٢٣٤٥٦'
    assert digits.convert_to_ar(123.456) == '١٢٣.٤٥٦'


def test_convert_to_en():
    assert digits.convert_to_en('۱۲۳٤٥٦') == '123456'


def test_conversion_function():
    assert digits._conversion('123', 'de') is None


def test_convert_to_word():
    assert digits.convert_to_word(500443) == 'پانصد هزار و چهارصد و چهل و سه'
    assert len(digits.convert_to_word(500)) == 5
    assert digits.convert_to_word(30000000000) == 'سی میلیارد'
    assert digits.convert_to_word(30000000000000) == 'سی بیلیون'
    assert digits.convert_to_word(30000000000000000) == 'سی بیلیارد'
    assert digits.convert_to_word(30000000000000000000) is None
    assert digits.convert_to_word(0) == 'صفر'

    assert digits.convert_to_word(500443, ordinal=True) == 'پانصد هزار و چهارصد و چهل و سوم'
    assert digits.convert_to_word(-30, ordinal=True) == 'منفی سی اُم'
    assert digits.convert_to_word(33, ordinal=True) == 'سی و سوم'
    assert digits.convert_to_word(45, ordinal=True) == 'چهل و پنجم'
