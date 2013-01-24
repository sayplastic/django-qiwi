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
from spyne.model.complex import XmlAttribute
from spyne.server.django import DjangoApplication
from spyne.protocol.xml import model

logger = logging.getLogger('django.qiwi')

def _checkLogin(login):
    return login == QIWI_LOGIN

def _checkPassword(password, txn):
    if password is None:
        return True
    secret_key = _getSecretKeyByTxn(txn)
    return secret_key == password

def _getSecretKeyByTxn(txn):
    return md5(
        str(txn) + md5(QIWI_PASSWORD).hexdigest().upper()
    ).hexdigest().upper()


#### MONKEYPATCH ####
def new_get_members_etree(prot, cls, inst, parent):
    delay = set()
    parent_cls = getattr(cls, '__extends__', None)
    if not (parent_cls is None):
        get_members_etree(prot, parent_cls, inst, parent)

    for k, v in cls._type_info.items():
        try:
            subvalue = getattr(inst, k, None)
        except: # to guard against sqlalchemy throwing NoSuchColumnError
            subvalue = None

        # This is a tight loop, so enable this only when necessary.
        # logger.debug("get %r(%r) from %r: %r" % (k, v, inst, subvalue))
        if issubclass(v, XmlAttribute):
            a_of = v._attribute_of
            if a_of is not None and a_of in cls._type_info.keys():
                attr_parent=parent.find("{%s}%s"%(cls.__namespace__,a_of))
                if attr_parent is None:
                    delay.add(k)
                else:
                    v.marshall(k,subvalue,attr_parent)
            else:
                v.marshall(k, subvalue, parent)
            continue

        mo = v.Attributes.max_occurs
        # For the love of god I couldn't figure out why does spyne put attributes
        # on SOAP result tag, so this ends here. Die, you friggin' namespace.
        cls.__namespace__ = ''
        if subvalue is not None and mo > 1:
            for sv in subvalue:
                prot.to_parent_element(v, sv, cls.get_namespace(), parent, k)

        # Don't include empty values for non-nillable optional attributes.
        elif subvalue is not None or v.Attributes.min_occurs > 0:
            prot.to_parent_element(v, subvalue, cls.get_namespace(), parent, k)

    for k in delay:
        v = cls._type_info[k]
        subvalue = getattr(inst, k, None)
        a_of = v._attribute_of
        attr_parent = parent.find("{%s}%s"%(cls.__namespace__,a_of))
        v.marshall(k,subvalue,attr_parent)

#### MONKEYPATCH ####
model.get_members_etree = new_get_members_etree


class QiwiService(ServiceBase):
    @srpc(String, String, String, Integer, _returns=Integer)
    def updateBill(login, password, txn, status):
        logger.debug('updateBill request from qiwi; login=%s, password=xxx, txn=%s, status=%s',
            login, txn, status)
        if _checkLogin(login) and _checkPassword(password, txn):
            response = update_bill(txn, status)
        else:
            logger.error('qiwi password mismatch for order %s', txn)
            response = 150
        logger.debug('order #%s: our response is %s', txn, response)
        return response


qiwi_django_application = csrf_exempt(DjangoApplication(
    Application([QiwiService],
        tns='http://client.ishop.mw.ru/',
        in_protocol=Soap11(),
        out_protocol=Soap11()
    )
))
