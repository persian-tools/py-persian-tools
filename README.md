# Persian Tools

An anthology of a variety of tools for the Persian language in Python

[![codecov](https://codecov.io/gh/persian-tools/py-persian-tools/branch/master/graph/badge.svg?token=0M7JehkAWU)](https://codecov.io/gh/persian-tools/py-persian-tools)
![Tests](https://github.com/persian-tools/py-persian-tools/workflows/Test/badge.svg)

## Installation

`pip install persian-tools`

## Modules

1. [digits](#digits)
2. [separator](#separator)
3. [ordinal suffix](#ordinal-suffix)
4. [bank](#bank)
    1. [card number](#card-number)
    2. [sheba](#sheba)
5. [national id](#national-id)
6. [legal id](#legal-id)
7. [phone number](#phone-number)
8. [bill](#bill)
9. [plate](#plate)

## Usage
Let's take a look at what an example test case would look like using `persian-tools`.

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

`persian-tools` also, has another function to convert numbers to words; you can convert result to ordinal mode with `ordinal=True` in inputs.
```python
from persian_tools import digits

digits.convert_to_word(500443)                  # پانصد هزار و چهارصد و چهل و سه
digits.convert_to_word(-500443)                 # منفی پانصد هزار و چهارصد و چهل و سه
digits.convert_to_word(500443, ordinal=True)    # پانصد هزار و چهارصد و چهل و سوم
digits.convert_to_word(30000000000)             # سی میلیارد
```

to convert words to number, you can use this function with different args:
```python
from persian_tools import digits

digits.convert_from_word('منفی سه هزارمین')                        # -3000
digits.convert_from_word('منفی سه هزارم', digits='fa')             # -۳۰۰۰
digits.convert_from_word('منفی سه هزار')                           # -3000
digits.convert_from_word('سه هزار دویست و دوازده')                 # 3212
digits.convert_from_word('دوازده هزار بیست دو', separator=True)    # '12,022'
digits.convert_from_word('حقوق شیش صد و ۲۷ میلیون تومان سالانه')    # 627000000
```

Note: as you can see in examples, this function will remove ordinal suffix by default.

### separator
Adding or removing thousands separators will handle; default separator is ',' but can change with second input.

```python
from persian_tools import separator

separator.add(300)                 # '300'
separator.add(3000000)             # '3,000,000'
separator.add(3000000.0003)        # '3,000,000.0003'
separator.add(3000000, '/')        # '3/000/000'
separator.add('۳۰۰۰۰')             # '۳۰,۰۰۰'

separator.remove('300')            # '300'
separator.remove('3,000,000')      # '3000000'
separator.remove('3/000/000', '/') # '3000000'
separator.remove('۳۰,۰۰۰')         # '۳۰۰۰۰'
```

### ordinal suffix
Adding or removing ordinal suffix for persian numbers in word will handle.

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
This module has useful functions related to bank cards number, like:
* validating them
* find bank data of a card number
* extract card numbers from a text

```python
from persian_tools.bank import card_number

card_number.validate('6037701689095443')    # True
card_number.validate('6219861034529007')    # True
card_number.validate('6219861034529008')    # False

card_number.bank_data('6219861034529007')
# {'nickname': 'saman', 'name': 'Saman Bank', 'persian_name': 'بانک سامان', 'card_prefix': ['621986'], 'sheba_code': ['056']}
card_number.bank_data('6037701689095443')
# {'nickname': 'keshavarzi', 'name': 'Keshavarzi', 'persian_name': 'بانک کشاورزی', 'card_prefix': ['603770', '639217'], 'sheba_code': ['016']}



card_number.extract_card_numbers('''شماره کارتم رو برات نوشتم:
                                     6219-8610-3452-9007
                                     اینم یه شماره کارت دیگه ای که دارم
                                    ۵۰۲۲-۲۹۱۰-۷۰۸۷-۳۴۶۶                                     
                                    5022291070873466''',                # first argument is a text
                                    check_validation=True,              # a boolean that define you need only valid card numbers in result, default: True
                                    detect_bank_name=True,              # this will add bank name in result, default: False
                                    filter_valid_card_numbers=True)     # just valid card numbers will be in result; be careful to `check_validation` be also True, default: True
# result
# [
#    {'pure': '6219861034529007', 'base': '6219-8610-3452-9007', 'index': 1, 'is_valid': True,
#     'bank_data': {
#         'nickname': 'saman',
#         'name': 'Saman Bank',
#         'persian_name': 'بانک سامان',
#         'card_prefix': ['621986'],
#         'sheba_code': ['056'],
#     }},
#    {'pure': '5022291070873466', 'base': '5022291070873466', 'index': 3, 'is_valid': True,
#     'bank_data': {
#         'nickname': 'pasargad',
#         'name': 'Pasargad Bank',
#         'persian_name': 'بانک پاسارگاد',
#         'card_prefix': ['502229', '639347'],
#         'sheba_code': ['057'],
#     }},
# ]
```

#### sheba
`sheba` module contain 2 functions:
* validating them
* find bank data of a sheba number

```python

from persian_tools.bank import sheba

sheba.validate('IR820540102680020817909002')    # True
sheba.validate('IR01234567890123456789')        # False

sheba.bank_data('IR820540102680020817909002')
# {
#     'nickname': 'parsian',
#     'name': 'Parsian Bank',
#     'persian_name': 'بانک پارسیان',
#     'card_prefix': ['622106', '627884'],
#     'sheba_code': ['054'],
#     'account_number': '020817909002',
#     'formatted_account_number': '002-00817909-002'
# }
```

### national id
This module has useful functions related to iranian national id (code-e melli), like:
* validating them
* generate a random one
* find place of national id by the prefix of id

```python
from persian_tools import national_id

national_id.validate('0499370899')      # True
national_id.validate('0684159415')      # False

national_id.generate_random()           # '0458096784'
national_id.generate_random()           # '1156537101'

national_id.find_place('0906582709')    # {'code': ['089', '090'], 'city': 'کاشمر', 'province': 'خراسان رضوی'}
national_id.find_place('0643005846')    # {'code': ['064', '065'], 'city': 'بیرجند', 'province': 'خراسان جنوبی'}
```

### legal id
This module contains two functions to generate random iranian legal id (shenas-e melli) and validate any given id.

```python
from persian_tools import legal_id

legal_id.validate('10380284790')      # True
legal_id.validate('11053639140')      # False

legal_id.generate_random()            # '10100387143'
legal_id.generate_random()            # '77111986110'
```

### phone number
This module can validate, normalize and give you some data from a phone number.

```python
from persian_tools import phone_number

phone_number.validate('09123456789')        # True
phone_number.validate('+989123456789')      # True
phone_number.validate('989123456789')       # True
phone_number.validate('98912345678')        # False

phone_number.normalize('00989022002580')    # 09022002580
phone_number.normalize('+989022002580')     # 09022002580
phone_number.normalize('9022002580')        # 09022002580
phone_number.normalize('9022002580', '0')   # 09022002580
phone_number.normalize('9022002580', '+98') # 09022002580

phone_number.operator_data('09123456789')
# {'province': ['البرز', 'زنجان', 'سمنان', 'قزوین', 'قم', 'برخی از شهرستان های استان مرکزی'], 'base': 'تهران', 'type': ['permanent'], 'operator': 'همراه اول'}
phone_number.operator_data('09303456789')
# {'province': [], 'base': 'کشوری', 'type': ['permanent', 'credit'], 'operator': 'ایرانسل'}
```

### bill
With `bill_id` and `payment_id` (or just `barcode`), you can get detail of a `bill`.

```python
from persian_tools import bill

bill.get_detail(bill_id=7748317800142, payment_id=1770160)
# result
# {'amount': 1700,
#  'barcode': '77483178001420001770160',
#  'bill_id': 7748317800142,
#  'is_valid': True,
#  'is_valid_bill_id': True,
#  'is_valid_payment_id': True,
#  'payment_id': 1770160,
#  'type': 'تلفن ثابت'}

bill.get_detail(barcode='77483178001420001770160')
# same result

# default currency is set to Toman, but can change like as below
bill.get_detail(barcode='77483178001420001770160', currency=bill.CURRENCY_RIAL)
# result
# {'amount': 17000,
#  ...
```

### plate
Get information(province, category, type) about vehicles plate.

```python
from persian_tools import plate

plate.get_info('12D45147')
# result
# {'category': 'دیپلمات',
#   'province': 'مرکزی',
#   'template': '12D451ایران47',
#   'type': 'Car'}

plate.get_info('12345678')
# result
# {'category': None,
#  'province': 'مرکز تهران',
#  'template': '123-45678',
#  'type': 'Motorcycle'}

plate.is_valid('12D45147') # True
plate.is_valid('12345678') # True
plate.is_valid('1234567') # False
plate.is_valid('1204567') # False
```

Note: Plates that have farsi digits in them(like: الف، ب، ص) will be returned in this template:

`{first_two_digits}{plate_character}{next_three_digits}ایران{province_code}`
