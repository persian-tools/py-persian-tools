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
