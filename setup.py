#!/usr/bin/env python
#coding: utf-8
from distutils.core import setup
import sys


reload(sys).setdefaultencoding("UTF-8")


setup(
    name='django-qiwi',
    version='0.1.3',
    author='Ivan Petukhov',
    author_email='satels@gmail.com',
    packages=[
        'django_qiwi', 'django_qiwi.soap',
        'django_qiwi.management', 'django_qiwi.management.commands'
    ],
    url='http://satels.blogspot.com/2011/07/django-qiwi-django-soap.html',
    download_url = 'https://github.com/satels/django-qiwi/zipball/master',
    license = 'MIT license',
    description = u'Приложение для работы с qiwi.ru.'.encode('utf8'),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
    install_requires=['spyne==2.9.3', 'SOAPPy==0.12.5']
)
