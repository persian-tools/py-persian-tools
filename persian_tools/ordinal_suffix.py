def add(number: str) -> str:
    if number.endswith('ی'):
        return number + ' اُم'
    if number == 'یک':
        return number[:-2] + 'اول'
    if number.endswith('سه'):
        return number[:-2] + 'سوم'
    return number + 'م'


def remove(word: str) -> str:
    word = word.replace('مین', '')
    word = word.replace(' ام', '')
    word = word.replace(' اُم', '')

    if word.endswith('اول'):
        return word[:-3] + 'یک'
    if word.endswith('سوم'):
        return word[:-3] + 'سه'
    elif word.endswith('م'):
        return word[:-1]
    return word
