#encoding:utf8
from django.core.management.base import BaseCommand
from django_qiwi.soap.server import Server as QiwiServer


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        server = QiwiServer()
        server.runserver()
