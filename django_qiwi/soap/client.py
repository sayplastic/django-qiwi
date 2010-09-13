#coding:utf8
from dateutil import parser as dateutil_parser
from django_qiwi.conf import *
import SOAPpy


class Client(object):

    def __init__(self):
        self._client = SOAPpy.SOAPProxy(QIWI_SOAP_ISHOP_URL)

    def createBill(self, phone, amount, comment, txn, lifetime,
                   alarm=QIWI_ALARM, create=QIWI_CREATE):
        return self._client.createBill(
            login=QIWI_LOGIN,
            password=QIWI_PASSWORD,
            user=phone,
            amount=amount,
            comment=comment,
            txn=txn,
            lifetime=lifetime.strftime("%d.%m.%Y %H:%M:%S"),
            alarm=alarm,
            create=create
        )

    def cancelBill(self, txn):
        return self._client.cancelBill(
            login=QIWI_LOGIN,
            password=QIWI_PASSWORD,
            txn=txn,
        )

    def checkBill(self, txn):
        response = self._client.checkBill(
            login=QIWI_LOGIN,
            password=QIWI_PASSWORD,
            txn=txn,
        )
        return {
            'phone': response.user,
            'amount': float(response.amount),
            'date': dateutil_parser.parse(response.date),
            'lifetime': dateutil_parser.parse(response.lifetime),
            'status': response.status,
        }
