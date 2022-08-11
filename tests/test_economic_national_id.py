from persian_tools import economic_national_id


def test_validate_economic_national_id():
    # These economic national ids are valid and registered
    assert economic_national_id.validate('10380284790')
    assert economic_national_id.validate('10100387143')
    
    # These economic national ids are all valid
    assert economic_national_id.validate('77111986110')
    assert economic_national_id.validate('18061055669')
    assert economic_national_id.validate('15292247120')
    assert economic_national_id.validate('42118547230')
    assert economic_national_id.validate('27388385445')    

    assert economic_national_id.validate('55828465992')
    assert economic_national_id.validate('32882926778')
    assert economic_national_id.validate('97006806007')
    assert economic_national_id.validate('21272129339')
    assert economic_national_id.validate('18706641333')

    # These economic national ids are all invalid
    assert economic_national_id.validate('84735069516') is False
    assert economic_national_id.validate('65399567978') is False
    assert economic_national_id.validate('99969101031') is False
    assert economic_national_id.validate('15826563190') is False
    assert economic_national_id.validate('11053639140') is False
    assert economic_national_id.validate('18090089802') is False


def test_generate_random_economic_national_id():
    for _ in range(15):
        assert economic_national_id.validate(economic_national_id.generate_random())
