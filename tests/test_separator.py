from persian_tools import separator


def test_add_separator():
    assert separator.add(1000000) == '1,000,000'
    assert separator.add(100000.0) == '100,000.0'
    assert separator.add(100000.0001) == '100,000.0001'
    assert separator.add('some text 1000000') == 'some text 1,000,000'
    assert separator.add('۱۲۳۴۵۶۷۸۹۰', '٫') == '۱٫۲۳۴٫۵۶۷٫۸۹۰'
    assert separator.add('١٢٣٤٥٦٧٨٩٠') == '١,٢٣٤,٥٦٧,٨٩٠'

    assert separator.add('') == ''
    assert separator.add(0) == '0'


def test_remove_separator():
    assert separator.remove('1,000,000') == '1000000'
    assert separator.remove('100,000.0') == '100000.0'
    assert separator.remove('some text 1,000,000') == 'some text 1000000'
    assert separator.remove('۱٫۲۳۴٫۵۶۷٫۸۹۰', '٫') == '۱۲۳۴۵۶۷۸۹۰'
    assert separator.remove('١,٢٣٤,٥٦٧,٨٩٠') == '١٢٣٤٥٦٧٨٩٠'
