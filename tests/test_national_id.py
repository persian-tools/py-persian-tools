from persian_tools import national_id


def test_verify_national_id():
    # this national id is equal to 0068415941
    assert national_id.verify('068415941')

    # this national id is equal to 0123000000
    assert national_id.verify('123000000') is False
    assert national_id.verify('0000000000') is False
    assert national_id.verify('4271427685') is False
    assert national_id.verify('0200203041') is False
    assert national_id.verify('0684159415') is False

    assert national_id.verify('0499370899')
    assert national_id.verify('0790419904')
    assert national_id.verify('0084575948')
    assert national_id.verify('0963695398')
    assert national_id.verify('0684159414')

    assert national_id.verify('0067749828')
    assert national_id.verify('0650451252')
    assert national_id.verify('1583250689')
    assert national_id.verify('4032152314')
    assert national_id.verify('0076229645')


def test_generate_random_national_id():
    for _ in range(15):
        assert national_id.verify(national_id.generate_random())
