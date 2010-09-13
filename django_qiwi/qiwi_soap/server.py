#coding:utf8
from django_qiwi import update_bill
from django_qiwi.conf import *
from hashlib import md5
import SOAPpy


def updateBill(login, password, txn, status):
    if _checkLogin(login) and _checkPassword(password, txn):
        update_bill(txn, status)

def _checkLogin(login):
    return login == QIWI_LOGIN

def _checkPassword(password, txn):
    secret_key = md5(txn + md5(QIWI_PASSWORD).upper()).upper()
    return secret_key == password


class Server(object):

    def __init__(self):
        self._server = SOAPpy.SOAPServer(QIWI_SOAP_SERVER)
        self._server.registerFunction(updateBill)

    def runserver(self):
        self._server.serve_forever()

