#coding:utf8
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module
from django_qiwi.conf import *


def get_qiwi_app():
    qiwi_app = QIWI_APP
    if qiwi_app not in settings.INSTALLED_APPS:
        raise ImproperlyConfigured(
            u"QIWI_APP (%r) должен быть установлен в INSTALLED_APPS" % qiwi_app
        )
    try:
        package = import_module(qiwi_app)
    except ImportError:
        raise ImproperlyConfigured(
            u"QIWI_APP ссылается на несуществующий пакет."
        )
    return package


def update_bill(txn, status):
    qiwi_package = get_qiwi_app()
    if hasattr(qiwi_package, "update_bill"):
        qiwi_package.update_bill(txn, status)
    else:
        raise ImproperlyConfigured(
            u"Задайте функцию update_bill(txn, status) в пакете QIWI_APP (%r)" % \
                QIWI_APP
        )
