#coding: utf-8

from hashlib import md5
from urllib import urlencode
from django import forms

from django_qiwi.conf import *


class QiwiBillForm(forms.Form):
    login = forms.CharField(max_length=20, initial=QIWI_LOGIN)
    to = forms.CharField(max_length=20)
    summ = forms.DecimalField()
    com = forms.CharField(max_length=255)
    lifetime = forms.DateTimeField()
    check_agt = forms.IntegerField(initial=QIWI_CREATE)
    txn_id = forms.CharField(max_length=20)
    currency = forms.IntegerField(initial=QIWI_CURRENCY)

    target = QIWI_HTTP_URL

    def __init__(self, *args, **kwargs):
        super(QiwiBillForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget = forms.HiddenInput()
        self.fields['from'] = self.fields['login']
        del self.fields['login']

    def get_redirect_url(self):
        def _initial(name, field):
            val = self.initial.get(name, field.initial)
            if not val:
                return val
            val = u'{}'.format(val)
            return val.encode('utf-8')

        fields = [(name, _initial(name, field))
                  for name, field in self.fields.items()
                  if _initial(name, field)
                 ]
        params = urlencode(fields)
        return '{}?{}'.format(self.target, params)

