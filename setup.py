#!/usr/bin/env python
#coding: utf-8
from distutils.core import setup
import sys


reload(sys).setdefaultencoding("UTF-8")


setup(
    name='django-qiwi',
    version='0.1.1',
    author='Ivan Petukhov',
    author_email='satels@gmail.com',
    packages=[
        'django_qiwi', 'django_qiwi.soap',
        'django_qiwi.management', 'django_qiwi.management.commands'
    ],
    license = 'MIT license',
    description = u'Приложение для работы с qiwi.ru.'.encode('utf8'),
    classifiers=(
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
