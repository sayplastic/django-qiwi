#encoding:utf8
from django.core.management.base import NoArgsCommand
from django_qiwi.soap.server import Server as QiwiServer


class Command(NoArgsCommand):

    def handle(self, *args, **kwargs):
        server = QiwiServer()
        server.runserver()
