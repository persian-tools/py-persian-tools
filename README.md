# Py Persian Tools

An anthology of a variety of tools for the Persian language in Python

[![codecov](https://codecov.io/gh/persian-tools/py-persian-tools/branch/master/graph/badge.svg?token=0M7JehkAWU)](https://codecov.io/gh/persian-tools/py-persian-tools)
![Tests](https://github.com/persian-tools/py-persian-tools/workflows/Test/badge.svg)

## Installation

_soon on pypi_

## Modules

1. [digits](#digits)
2. [commas](#commas)
3. [ordinal suffix](#ordinal-suffix)
4. [bank](#bank)
    1. [card number](#card-number)
    2. [sheba](#sheba)
5. [national id](#national-id)

## Usage
### digits
This module will help you to normalize digits from Persian, Arabic and English to only one of them.

```python
from persian_tools import digits

digits.convert_to_fa(123)          # '۱۲۳'
digits.convert_to_fa('123')        # '۱۲۳'
digits.convert_to_fa('123٤٥٦')     # '۱۲۳۴۵۶'
digits.convert_to_fa('sth 123٤٥٦') # 'sth ۱۲۳۴۵۶'

digits.convert_to_en('۱۲۳')        # '123'
digits.convert_to_en('۱۲۳٤٥٦')     # '123456'
digits.convert_to_en('sth ۱۲۳٤٥٦') # 'sth 123456'

digits.convert_to_ar(123)          # '۱۲۳'
digits.convert_to_ar('123')        # '۱۲۳'
digits.convert_to_ar('sth 123۴۵۶') # 'sth ۱۲۳٤٥٦'
```

### commas
Adding or removing commas will handle; also separator can change in second argument

```python
from persian_tools import commas

commas.add(300)                 # '300'
commas.add(3000000)             # '3,000,000'
commas.add(3000000, '/')        # '3/000/000'
commas.add('۳۰۰۰۰')             # '۳۰,۰۰۰'

commas.remove('300')            # '300'
commas.remove('3,000,000')      # '3000000'
commas.remove('3/000/000', '/') # '3000000'
commas.remove('۳۰,۰۰۰')         # '۳۰۰۰۰'
```

### ordinal suffix
Adding or removing ordinal suffix will handle

```python
from persian_tools import ordinal_suffix

ordinal_suffix.add('بیست')          # 'بیستم'
ordinal_suffix.add('سی و سه')       # 'سی و سوم'
ordinal_suffix.add('سی')            # 'سی اُم'

ordinal_suffix.remove('دومین')      # 'دو'
ordinal_suffix.remove('سی و سوم')   # 'سی و سه'
ordinal_suffix.remove('بیستم')      # 'بیست'
ordinal_suffix.remove('سی اُم')      # 'سی'
```

### bank
#### card number
This module has useful functions related to bank cards number

```python
from persian_tools.bank import card_number

card_number.validate('6037701689095443')    # True
card_number.validate('6219861034529007')    # True
card_number.validate('6219861034529008')    # False

card_number.bank_name('6037701689095443')   # 'بانک کشاورزی'
card_number.bank_name('6219861034529007')   # 'بانک سامان'
card_number.bank_name('6219861034529007')   # 'بانک سامان'

card_number.extract_card_numbers('''شماره کارتم رو برات نوشتم:
                                     6219-8610-3452-9007
                                     اینم یه شماره کارت دیگه ای که دارم
                                     5022291070873466
                                     ۵۰۲۲۲۹۱۰۸۱۸۷۳۴۶۶
                                     ۵۰۲۲-۲۹۱۰-۷۰۸۷-۳۴۶۶''',            # first argument is a text
                                    check_validation=True,              # a boolean that define you need only valid card numbers in result, default: True
                                    detect_bank_name=True,              # this will add bank name in result, default: False
                                    filter_valid_card_numbers=True)     # just valid card numbers will be in result; be careful to `check_validation` be also True, default: True
# result
# [
#     {'pure': '6219861034529007', 'base': '6219-8610-3452-9007', 'index': 1, 'is_valid': True, 'bank_name': 'بانک سامان'},
#     {'pure': '5022291070873466', 'base': '5022291070873466', 'index': 2, 'is_valid': True, 'bank_name': 'بانک پاسارگاد'},
#     {'pure': '5022291070873466', 'base': '۵۰۲۲-۲۹۱۰-۷۰۸۷-۳۴۶۶', 'index': 4, 'is_valid': True, 'bank_name': 'بانک پاسارگاد'}
# ]
```

#### sheba
*soon*

### national id
This module has useful functions related to national id

```python
from persian_tools import national_id

national_id.validate('0499370899')      # True
national_id.validate('0684159415')      # False

national_id.generate_random()           # '0458096784'
national_id.generate_random()           # '1156537101'

national_id.find_place('0906582709')    # {'code': ['089', '090'], 'city': 'کاشمر', 'province': 'خراسان رضوی'}
national_id.find_place('0643005846')    # {'code': ['064', '065'], 'city': 'بیرجند', 'province': 'خراسان جنوبی'}
```
