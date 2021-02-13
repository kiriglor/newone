from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=12)
    password = models.CharField(max_length=20)

