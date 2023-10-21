from persian_tools import ordinal_suffix


def test_add_ordinal_suffix():
    assert ordinal_suffix.add('چهل و سه') == 'چهل و سوم'
    assert ordinal_suffix.add('چهل و پنج') == 'چهل و پنجم'
    assert ordinal_suffix.add('سی') == 'سی اُم'
    assert ordinal_suffix.add('یک') == 'اول'
    assert ordinal_suffix.add('چهل و یک') == 'چهل و یکم'


def test_remove_ordinal_suffix():
    assert ordinal_suffix.remove('چهل و سوم') == 'چهل و سه'
    assert ordinal_suffix.remove('چهل و پنجم') == 'چهل و پنج'
    assert ordinal_suffix.remove('سی اُم') == 'سی'
    assert ordinal_suffix.remove('اول') == 'یک'
    assert ordinal_suffix.remove('یکم') == 'یک'
    assert ordinal_suffix.remove('چهل و یکم') == 'چهل و یک'
