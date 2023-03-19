from persian_tools import legal_id


def test_validate_legal_id():
    # These legal ids are valid and registered
    assert legal_id.validate('10380284790')
    assert legal_id.validate('10100387143')

    # These legal ids are all valid
    assert legal_id.validate('77111986110')
    assert legal_id.validate('18061055669')
    assert legal_id.validate('15292247120')
    assert legal_id.validate('42118547230')
    assert legal_id.validate('27388385445')

    assert legal_id.validate('55828465992')
    assert legal_id.validate('32882926778')
    assert legal_id.validate('97006806007')
    assert legal_id.validate('21272129339')
    assert legal_id.validate('18706641333')

    # These legal ids are all invalid
    assert legal_id.validate('84735069516') is False
    assert legal_id.validate('65399567978') is False
    assert legal_id.validate('99969101031') is False
    assert legal_id.validate('15826563190') is False
    assert legal_id.validate('11053639140') is False
    assert legal_id.validate('18090089802') is False
    assert legal_id.validate('123001000') is False
    assert legal_id.validate('11111111111') is False
    assert legal_id.validate('10380284792') is False
    assert legal_id.validate('10380285692') is False
    assert legal_id.validate('09748208301') is False
    assert legal_id.validate('097482083013') is False
    assert legal_id.validate('0974820830a') is False


def test_generate_random_legal_id():
    for _ in range(15):
        assert legal_id.validate(legal_id.generate_random())
