#encoding:utf8
from django.core.management.base import NoArgsCommand
from django_qiwi.soap.server import runserver


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        runserver()
