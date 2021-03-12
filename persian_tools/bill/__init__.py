from typing import Union
from .exceptions import NotEnoughArguments

TYPES = {
    1: "آب",
    2: "برق",
    3: "گاز",
    4: "تلفن ثابت",
    5: "تلفن همراه",
    6: "عوارض شهرداری",
    8: "سازمان مالیات",
    9: "جرایم راهنمایی و رانندگی",
}

CURRENCY_TOMAN = 100
CURRENCY_RIAL = 1000


def _cal_the_bit(num: str) -> int:
    _sum = 0
    base = 2

    for i in range(len(num)):
        if base == 8:
            base = 2

        sub_str = num[-1 - i]
        _sum += int(sub_str) * base

        base += 1

    _sum %= 11
    if _sum < 2:
        return 0
    else:
        return 11 - _sum


def get_detail(bill_id: Union[int, None] = None, payment_id: Union[int, None] = None, barcode: Union[str, None] = None,
               currency: str = CURRENCY_TOMAN) -> dict:
    if bill_id and payment_id:
        barcode = str(bill_id) + '000' + str(payment_id)
    elif barcode:
        bill_id = int(barcode[:13])
        payment_id = int(barcode[16:26])
    else:
        raise NotEnoughArguments()

    def verification_payment_id():
        str_bill_id = str(bill_id)
        str_payment_id = str(payment_id)

        if not str_payment_id or len(str_payment_id) < 6:
            return False

        control_bit1 = str_payment_id[len(str_payment_id) - 2]
        control_bit2 = str_payment_id[len(str_payment_id) - 1]
        control_payment_id = str_payment_id[:len(str_payment_id) - 2]

        return _cal_the_bit(control_payment_id) == int(control_bit1) and \
               _cal_the_bit(str_bill_id + control_payment_id + control_bit1) == int(control_bit2)

    valid_payment_id = verification_payment_id()

    amount = None
    if valid_payment_id:
        amount = int(str(payment_id)[:-5]) * currency

    bill_type = TYPES.get(int(str(bill_id)[-2:-1]))

    def verification_bill_id():
        str_bill_id = str(bill_id)

        if not str_bill_id or len(str_bill_id) < 6:
            return False

        control_bit = str_bill_id[-1]

        new_str_bill_id = str_bill_id[:-1]
        return _cal_the_bit(new_str_bill_id) == int(control_bit) and bill_type is not None

    valid_bill_id = verification_bill_id()

    valid_bill_data = valid_bill_id and valid_payment_id

    return {
        'amount': amount,
        'type': bill_type,
        'barcode': barcode,
        'bill_id': bill_id,
        'payment_id': payment_id,
        'is_valid': valid_bill_data,
        'is_valid_bill_id': valid_bill_id,
        'is_valid_payment_id': valid_payment_id,
    }
