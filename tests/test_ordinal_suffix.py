from persian_tools import ordinal_suffix


def test_add_ordinal_suffix():
    assert ordinal_suffix.add('چهل و سه') == 'چهل و سوم'
    assert ordinal_suffix.add('چهل و پنج') == 'چهل و پنجم'
    assert ordinal_suffix.add('سی') == 'سی اُم'


def test_remove_ordinal_suffix():
    assert ordinal_suffix.remove('چهل و سوم') == 'چهل و سه'
    assert ordinal_suffix.remove('چهل و پنجم') == 'چهل و پنج'
    assert ordinal_suffix.remove('سی اُم') == 'سی'
