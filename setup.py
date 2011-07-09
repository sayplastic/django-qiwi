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
    license = 'MIT license',
    description = u'Приложение для работы с qiwi.ru.'.encode('utf8'),
    classifiers=(
        'Development Status :: 1',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
    install_requires=['soaplib==0.8.1', 'SOAPPy==0.12.0']
)
