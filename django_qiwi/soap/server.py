#coding:utf8
from django_qiwi import update_bill
from django_qiwi.conf import *
from hashlib import md5
from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod
from soaplib.serializers.primitive import String, Integer, Array


def _checkLogin(login):
    return login == QIWI_LOGIN

def _checkPassword(password, txn):
    secret_key = md5(
        str(txn) + md5(QIWI_PASSWORD).hexdigest().upper()
    ).hexdigest().upper()
    return secret_key == password


class QiwiServerService(SimpleWSGISoapApp):

    @soapmethod(String, String, String, Integer, _returns=Integer)
    def updateBill(self, login, password, txn, status):
        if _checkLogin(login) and _checkPassword(password, txn):
            response = update_bill(txn, status)
        else:
            response = 150
        return response


def runserver():
    from wsgiref.simple_server import make_server
    server = make_server('tutpokupki.ru', 17777, QiwiServerService())
    server.serve_forever()
