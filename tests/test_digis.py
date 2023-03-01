from persian_tools import digits


def test_convert_to_fa():
    assert digits.convert_to_fa('123٤٥٦') == '۱۲۳۴۵۶'
    assert digits.convert_to_fa(123456) == '۱۲۳۴۵۶'


def test_convert_to_ar():
    assert digits.convert_to_ar('123۴۵۶') == '١٢٣٤٥٦'
    assert digits.convert_to_ar(123.456) == '١٢٣.٤٥٦'


def test_convert_to_en():
    assert digits.convert_to_en('۱۲۳٤٥٦') == '123456'


def test_chaining_behavior():
    assert digits.convert_to_en(digits.convert_to_fa('123٤٥٦')) == '123456'


def test_conversion_function():
    assert digits._conversion('123', 'de') is None


def test_convert_to_word():
    assert digits.convert_to_word(500443) == 'پانصد هزار و چهارصد و چهل و سه'
    assert digits.convert_to_word(987654321) == \
           'نهصد و هشتاد و هفت میلیون و ششصد و پنجاه و چهار هزار و سیصد و بیست و یک'
    assert len(digits.convert_to_word(500)) == 5
    assert digits.convert_to_word(30000000000) == 'سی میلیارد'
    assert digits.convert_to_word(30000000000000) == 'سی بیلیون'
    assert digits.convert_to_word(30000000000000000) == 'سی بیلیارد'
    assert digits.convert_to_word(300000000000000000000) is None
    assert digits.convert_to_word(0) == 'صفر'
    assert digits.convert_to_word(4) == 'چهار'
    assert digits.convert_to_word(33) == 'سی و سه'

    assert digits.convert_to_word(500443, ordinal=True) == 'پانصد هزار و چهارصد و چهل و سوم'
    assert digits.convert_to_word(-30, ordinal=True) == 'منفی سی اُم'
    assert digits.convert_to_word(-123, ordinal=True) == 'منفی صد و بیست و سوم'
    assert digits.convert_to_word(33, ordinal=True) == 'سی و سوم'
    assert digits.convert_to_word(45, ordinal=True) == 'چهل و پنجم'


def test_convert_from_word():
    assert digits.convert_from_word('') is None
    assert digits.convert_from_word(None) is None
    assert digits.convert_from_word('متن بدون عدد') == 0
    assert digits.convert_from_word('صفر') == 0

    assert digits.convert_from_word('منفی سه هزار') == -3000
    assert digits.convert_from_word('سه هزار دویست و دوازده') == 3212
    assert digits.convert_from_word('دوازده هزار بیست دو') == 12022
    assert digits.convert_from_word('دوازده هزار بیست دو', separator=True) == '12,022'
    assert digits.convert_from_word('دوازده هزار و بیست و دو', separator=True) == '12,022'
    assert digits.convert_from_word('شیش صد و بیست و هفت') == 627
    assert digits.convert_from_word('حقوق شیش صد و ۲۷ میلیون تومان سالانه') == 627 * 1000 * 1000


def test_convert_from_word_to_ar():
    assert digits.convert_from_word("منفی سه هزار", digits="ar") == "-٣٠٠٠"
    assert digits.convert_from_word("سه هزار دویست و دوازده", digits="ar") == "٣٢١٢"
    assert digits.convert_from_word("دوازده هزار بیست دو", digits="ar") == "١٢٠٢٢"
    assert digits.convert_from_word("دوازده هزار بیست دو", digits="ar", separator=True) == "١٢,٠٢٢"
    assert digits.convert_from_word("دوازده هزار و بیست و دو", digits="ar", separator=True) == "١٢,٠٢٢"
    assert digits.convert_from_word("چهارصد پنجاه هزار", digits="ar", separator=True) == "٤٥٠,٠٠٠"
    assert digits.convert_from_word("چهارصد پنجاه هزار", digits="ar") == "٤٥٠٠٠٠"


def test_convert_from_word_with_ordinal():
    assert digits.convert_from_word("منفی ۳ هزار", digits="fa", separator=True) == "-۳,۰۰۰"
    assert digits.convert_from_word("منفی 3 هزار و 200", digits="fa", separator=True) == "-۳,۲۰۰"
    assert digits.convert_from_word("منفی سه هزارمین", digits="fa", separator=True) == "-۳,۰۰۰"
    assert digits.convert_from_word("منفی سه هزارمین", digits="fa") == "-۳۰۰۰"
    assert digits.convert_from_word("منفی سه هزارمین") == -3000
    assert digits.convert_from_word("منفی سه هزارم") == -3000
    assert digits.convert_from_word("منفی سه هزارمین") != "-3000"
    assert len(str(digits.convert_from_word("منفی سه هزارمین"))) == 5
    assert digits.convert_from_word("منفی سی اُم") == -30
    assert digits.convert_from_word("سی و سوم") == 33
