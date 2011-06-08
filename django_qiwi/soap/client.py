#coding:utf8
import datetime
import decimal
import SOAPpy
from django_qiwi.conf import *


class Client(object):

    def __init__(self):
        self._client = SOAPpy.SOAPProxy(QIWI_SOAP_ISHOP_URL)

    def createBill(self, phone, amount, comment, txn, lifetime,
                   alarm=QIWI_ALARM, create=QIWI_CREATE):
        response = self._client.createBill(
            login=QIWI_LOGIN,
            password=QIWI_PASSWORD,
            user=phone,
            amount=amount,
            comment=comment,
            txn=txn,
            lifetime=_format_datetime(lifetime),
            alarm=alarm,
            create=create
        )
        return int(response)

    def cancelBill(self, txn):
        response = self._client.cancelBill(
            login=QIWI_LOGIN,
            password=QIWI_PASSWORD,
            txn=txn,
        )
        return int(response)

    def checkBill(self, txn):
        response = self._client.checkBill(
            login=QIWI_LOGIN,
            password=QIWI_PASSWORD,
            txn=txn,
        )
        return {
            'phone': response.user,
            'amount': _parse_amount(response.amount),
            'date': _parse_datetime(response.date),
            'lifetime': _parse_datetime(response.lifetime),
            'status': abs(int(response.status)),
        }


def _parse_amount(amount):
    if not amount:
        return None

    return decimal.Decimal(amount)


_DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'

def _parse_datetime(s):
    if not s:
        return None

    return datetime.datetime.strptime(s, _DATETIME_FORMAT)


def _format_datetime(d):
    if not d:
        return ''

    return d.strftime(_DATETIME_FORMAT)

