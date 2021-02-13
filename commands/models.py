from django.db import models


class Sportsman (models.Model):
    fullname = models.CharField(max_length=30)
    def __str__(self):
        return self.fullname

class Command(models.Model):
    command_name = models.CharField(max_length=12, unique=True)
    group_members = models.ManyToManyField(Sportsman, verbose_name='участники', related_name='group_members')


    def __str__(self):
        return self.command_name