#coding: utf-8

from hashlib import md5
from urllib import urlencode
from django import forms

from django_qiwi.conf import *


class RobokassaForm(BaseRobokassaForm):
    from = forms.CharField(max_length=20, initial=QIWI_LOGIN)
    to = forms.CharField(max_length=20)
    summ = forms.DecimalField()
    com = forms.CharField(max_length=255)
    lifetime = forms.DateTimeField()
    check_agt = forms.IntegerField(initial=QIWI_CREATE)
    txn_id = forms.CharField(max_length=20)
    currency = forms.IntegerField(max_length=20, initial=QIWI_CURRENCY)

    target = QIWI_HTTP_URL

    def __init__(self, *args, **kwargs):
        super(RobokassaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget = forms.HiddenInput()

    def get_redirect_url(self):
        def _initial(name, field):
            val = self.initial.get(name, field.initial)
            if not val:
                return val
            return unicode(val)#.encode('1251')

        fields = [(name, _initial(name, field))
                  for name, field in self.fields.items()
                  if _initial(name, field)
                 ]
        params = urlencode(fields)
        return '{}?{}'.format(self.target, params)

