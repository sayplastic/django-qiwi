#coding:utf8
from django.conf import settings


QIWI_APP = getattr(settings, 'QIWI_APP')
QIWI_SOAP_ISHOP_URL = getattr(settings, 'QIWI_SOAP_ISHOP_URL', 'https://ishop.qiwi.ru/services/ishop')
QIWI_HTTP_URL = getattr(settings, 'QIWI_HTTP_URL', 'http://w.qiwi.ru/setInetBill_utf.do')
QIWI_LOGIN = getattr(settings, 'QIWI_LOGIN')
QIWI_PASSWORD = getattr(settings, 'QIWI_PASSWORD')
QIWI_CREATE  = getattr(settings, 'QIWI_CREATE', 0)
QIWI_ALARM  = getattr(settings, 'QIWI_ALARM', 0)
QIWI_SOAP_SERVER = getattr(settings, 'QIWI_SOAP_SERVER')
QIWI_CURRENCY  = getattr(settings, 'QIWI_CURRENCY', 643) # RUR

