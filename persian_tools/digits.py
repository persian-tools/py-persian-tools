from typing import Union
from . import LANGUAGES

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
