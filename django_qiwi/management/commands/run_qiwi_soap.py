#encoding:utf8
from django.core.management.base import NoArgsCommand
from django_qiwi.qiwi_soap.server import Server as QiwiServer


class Command(NoArgsCommand):

    server = QiwiServer()
    server.runserver()
