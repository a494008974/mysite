from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    # password = models.CharField(_('password'), max_length=128)