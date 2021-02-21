from typing import Union
import re


def add(number: Union[int, float, str], separator: str = ',') -> str:
    number = str(number)
    parts = number.split('.')
    pattern = '(\\d)(?=(\\d{3})+(?!\\d))'
    repl = r'\1{sep}'.format(sep=separator)

    parts[0] = re.sub(pattern, repl, parts[0])
    return '.'.join(parts)


def remove(number: str, separator: str = ',') -> str:
    return str(number).replace(separator, '')
