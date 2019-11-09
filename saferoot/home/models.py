from django.db import models

# Create your models here.
class dict_database(models.Model):
    key = models.IntegerField()
    dict_key = {'hello': 9}
