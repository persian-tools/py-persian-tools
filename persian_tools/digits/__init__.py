from typing import Union
from math import floor
from .strings import SCALE, NUMBER_TEXT, TYPO_LIST, JOINERS, PREFIXES, UNITS, TEN, MAGNITUDE
from ..ordinal_suffix import add as add_ordinal_suffix, remove as remove_ordinal_suffix
from ..separator import add as add_separator


class LANGUAGES:
    EN = 'en'
    FA = 'fa'
    AR = 'ar'


SUPPORTED_CHARS = {
    LANGUAGES.EN: '0123456789',
    LANGUAGES.FA: '۰۱۲۳۴۵۶۷۸۹',
    LANGUAGES.AR: '٠١٢٣٤٥٦٧٨٩',
}


def _conversion(number: Union[int, float, str],
                destination_lang: str = LANGUAGES.FA) -> Union[str, None]:
    if destination_lang not in SUPPORTED_CHARS.keys():
        return None

    result = str(number)

    source_chars = SUPPORTED_CHARS.copy()
    destination_chars = source_chars.pop(destination_lang)
    for chars in source_chars.values():
        for i in range(10):
            result = result.replace(chars[i], destination_chars[i])

    return result


def convert_to_fa(number: Union[int, float, str]) -> Union[str, None]:
    return _conversion(number, LANGUAGES.FA)


def convert_to_ar(number: Union[int, float, str]) -> Union[str, None]:
    return _conversion(number, LANGUAGES.AR)


def convert_to_en(number: Union[int, float, str]) -> Union[str, None]:
    return _conversion(number, LANGUAGES.EN)


def convert_to_word(number: int, ordinal: bool = False) -> Union[str, None]:
    def to_word(num: int) -> str:
        res = ''
        for unit in [100, 10, 1]:
            if floor(num / unit) * unit != 0:
                if num in NUMBER_TEXT.keys():
                    res += NUMBER_TEXT[num]
                    break
                else:
                    res += NUMBER_TEXT[floor(num / unit) * unit] + ' و '
                    num %= unit

        return res

    if number == 0:
        return 'صفر'

    is_negative = number < 0
    number = abs(number)

    base = 1000
    result = []
    while number > 0:
        result.append(to_word(number % base))
        number = floor(number / base)

    if len(result) > 6:
        return None

    for i in range(len(result)):
        if result[i] != '':
            result[i] += ' ' + SCALE[i] + ' و '

    result = list(reversed(result))
    words = ''.join(result)

    while words.endswith(' و '):
        words = words[:-3]

    if is_negative:
        words = 'منفی ' + words

    words = words.strip()

    if ordinal:
        words = add_ordinal_suffix(words)

    return words


def convert_from_word(text: Union[str, None], digits: str = LANGUAGES.EN, separator: bool = False) -> Union[str, None]:
    def tokenize(_text: str) -> list:
        for typo in TYPO_LIST.keys():
            if typo in _text:
                _text = _text.replace(typo, TYPO_LIST[typo])

        slitted_text = _text.split(' ')
        slitted_text = [txt for txt in slitted_text if txt != JOINERS[0]]

        return slitted_text

    def compute(tokens: list) -> int:
        result = 0
        is_negative = False

        for token in tokens:
            token = convert_to_en(token)

            if token == PREFIXES[0]:
                is_negative = True
            elif UNITS.get(token):
                result += UNITS[token]
            elif TEN.get(token):
                result += TEN[token]
            elif token.isdigit():
                result += int(token)
            elif MAGNITUDE.get(token):
                result *= MAGNITUDE[token]

        if is_negative:
            result *= -1

        return result

    if text == '' or text is None:
        return None

    text = remove_ordinal_suffix(text)

    computed = compute(tokenize(text))
    if separator:
        computed = add_separator(computed)

    if digits != LANGUAGES.EN:
        computed = _conversion(computed, digits)

    return computed
