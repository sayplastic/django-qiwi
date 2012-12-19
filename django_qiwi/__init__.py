#coding:utf8
import re

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module
from django_qiwi.conf import *
from django_qiwi.soap.utils import STATUS_CODE_TEXT
from django.dispatch import Signal


qiwi_update_bill = Signal(providing_args=['txn', 'status'])


def get_qiwi_app():
    qiwi_app = QIWI_APP
    # if qiwi_app not in settings.INSTALLED_APPS:
    #     raise ImproperlyConfigured(
    #         'QIWI_APP is set to %s which doesn\'t appear to beinstalled' % qiwi_app
    #     )
    try:
        package = import_module(qiwi_app)
    except ImportError:
        raise ImproperlyConfigured(
            'Cannot import %s' % qiwi_app
        )
    return package


def update_bill(txn, status):
    qiwi_package = get_qiwi_app()
    qiwi_update_bill.send(sender=update_bill, txn=txn, status=status)
    if hasattr(qiwi_package, "update_bill"):
        return qiwi_package.update_bill(txn, status)
    else:
        raise ImproperlyConfigured(
            'Define update_bill(txn, status) function in QIWI_APP (%r)' % QIWI_APP
        )


def get_status_text(code):
    return dict(STATUS_CODE_TEXT).get(code)


def process_phone(phone):
    return re.sub(r'\D', '', phone).lstrip('7')