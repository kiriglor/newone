from django.db import models
from commands.models import Command


class Match(models.Model):
    command_1 = models.ManyToManyField(Command, verbose_name='Команда 1', related_name='command_1')
    command_2 = models.ManyToManyField(Command, verbose_name='Команда 2', related_name='command_2')
