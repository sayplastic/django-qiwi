#coding:utf8
import logging
from django_qiwi import update_bill
from django_qiwi.conf import QIWI_LOGIN, QIWI_PASSWORD, QIWI_SOAP_SERVER
from hashlib import md5
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from spyne.protocol.soap import Soap11
from spyne.application import Application
from spyne.service import ServiceBase
from spyne.decorator import srpc
from spyne.model.primitive import String, Integer
from spyne.server.django import DjangoApplication


logger = logging.getLogger('django.qiwi')

def _checkLogin(login):
    return login == QIWI_LOGIN

def _checkPassword(password, txn):
    if password is None:
        return True
    secret_key = _getSecretKeyByTxn(txn)
    logger.debug('got credentials from qiwi, our key: %s, their key: %s', secret_key, password)
    return secret_key == password

def _getSecretKeyByTxn(txn):
    return md5(
        str(txn) + md5(QIWI_PASSWORD).hexdigest().upper()
    ).hexdigest().upper()


class QiwiService(ServiceBase):
    @srpc(String, String, String, Integer, _returns=Integer)
    def updateBill(login, password, txn, status):
        if _checkLogin(login) and _checkPassword(password, txn):
            response = update_bill(txn, status)
        else:
            response = 150
        return response


qiwi_django_application = csrf_exempt(DjangoApplication(
    Application([QiwiService],
        tns='qiwi.application.django',
        in_protocol=Soap11(),
        out_protocol=Soap11()
    )
))