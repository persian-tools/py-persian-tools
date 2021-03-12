from persian_tools import bill
from persian_tools.bill.exceptions import NotEnoughArguments
import pytest


def test_bill_amount():
    assert bill.get_detail(bill_id=1117753200140, payment_id=12070160, currency=bill.CURRENCY_RIAL).get(
        'amount') == 120000
    assert bill.get_detail(bill_id=1117753200140, payment_id=12070160).get('amount') == 12000
    assert bill.get_detail(bill_id=1177809000142, payment_id=570108, currency=bill.CURRENCY_RIAL).get('amount') == 5000
    assert bill.get_detail(bill_id=1177809000142, payment_id=570108).get('amount') == 500
    assert bill.get_detail(bill_id=7748317800142, payment_id=1770160, currency=bill.CURRENCY_RIAL).get(
        'amount') == 17000
    assert bill.get_detail(bill_id=7748317800142, payment_id=1770160).get('amount') == 1700


def test_bill_type():
    assert bill.get_detail(bill_id=7748317800142, payment_id=1770160, currency=bill.CURRENCY_RIAL).get(
        'type') == 'تلفن ثابت'
    assert bill.get_detail(bill_id=9174639504124, payment_id=12908197).get('type') == 'برق'
    assert bill.get_detail(bill_id=2050327604613, payment_id=1070189).get('type') == 'آب'
    assert bill.get_detail(bill_id=9100074409151, payment_id=12908190).get('type') == 'تلفن همراه'


def test_bill_id_validation():
    assert bill.get_detail(bill_id=7748317800142, payment_id=1770160).get('is_valid_bill_id') is True
    assert bill.get_detail(bill_id=9174639504124, payment_id=12908197).get('is_valid_bill_id') is True
    assert bill.get_detail(bill_id=2050327604613, payment_id=1070189).get('is_valid_bill_id') is True
    assert bill.get_detail(bill_id=2234322344613, payment_id=1070189).get('is_valid_bill_id') is False
    assert bill.get_detail(bill_id=2234, payment_id=1070189).get('is_valid_bill_id') is False


def test_bill_payment_id_validation():
    assert bill.get_detail(bill_id=7748317800142, payment_id=1770160).get('is_valid_payment_id') is True
    assert bill.get_detail(bill_id=9174639504124, payment_id=12908197).get('is_valid_payment_id') is False
    assert bill.get_detail(bill_id=2050327604613, payment_id=1070189).get('is_valid_payment_id') is True
    assert bill.get_detail(bill_id=2234322344613, payment_id=1070189).get('is_valid_payment_id') is False
    assert bill.get_detail(bill_id=2234322344613, payment_id=1070).get('is_valid_payment_id') is False


def test_bill_validation():
    assert bill.get_detail(bill_id=7748317800142, payment_id=1770160).get('is_valid') is True
    assert bill.get_detail(bill_id=9174639504124, payment_id=12908197).get('is_valid') is False
    assert bill.get_detail(bill_id=2050327604613, payment_id=1070189).get('is_valid') is True
    assert bill.get_detail(bill_id=2234322344613, payment_id=1070189).get('is_valid') is False


def test_find_bills_barcode():
    assert bill.get_detail(bill_id=7748317800142, payment_id=1770160).get('barcode') == '77483178001420001770160'
    assert bill.get_detail(bill_id=9174639504124, payment_id=12908197).get('barcode') == '917463950412400012908197'
    assert bill.get_detail(bill_id=2050327604613, payment_id=1070189).get('barcode') == '20503276046130001070189'
    assert bill.get_detail(bill_id=2234322344613, payment_id=1070189).get('barcode') == '22343223446130001070189'


def test_find_bills_id():
    bill_detail = bill.get_detail(barcode='22343223446130001070189')
    assert bill_detail.get('bill_id') == 2234322344613
    assert bill_detail.get('payment_id') == 1070189


def test_not_enough_arguments():
    with pytest.raises(NotEnoughArguments,
                       match='Arguments are not enough; we need `bill_id` and `payment_id` or at least, bill `barcode`'):
        bill.get_detail()
        bill.get_detail(bill_id=7748317800142)
