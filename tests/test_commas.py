from persian_tools import commas


def test_add_commas():
    assert commas.add(1000000) == '1,000,000'
    assert commas.add(100000.0) == '100,000.0'
    assert commas.add('some text 1000000') == 'some text 1,000,000'
    assert commas.add('۱۲۳۴۵۶۷۸۹۰', '٫') == '۱٫۲۳۴٫۵۶۷٫۸۹۰'
    assert commas.add('١٢٣٤٥٦٧٨٩٠') == '١,٢٣٤,٥٦٧,٨٩٠'


def test_remove_commas():
    assert commas.remove('1,000,000') == '1000000'
    assert commas.remove('100,000.0') == '100000.0'
    assert commas.remove('some text 1,000,000') == 'some text 1000000'
    assert commas.remove('۱٫۲۳۴٫۵۶۷٫۸۹۰', '٫') == '۱۲۳۴۵۶۷۸۹۰'
    assert commas.remove('١,٢٣٤,٥٦٧,٨٩٠') == '١٢٣٤٥٦٧٨٩٠'
