from typing import Union
import re


def add(number: Union[int, float, str], separator: str = ',') -> str:
    pattern = '(\\d)(?=(\\d{3})+(?!\\d))'
    repl = r'\1{sep}'.format(sep=separator)
    result = str(number)
    return re.sub(pattern, repl, result)


def remove(number: str, separator: str = ',') -> str:
    return str(number).replace(separator, '')
