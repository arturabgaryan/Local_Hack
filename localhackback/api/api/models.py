from django.db import models

# Create your models here.


class Day(models.Model):
    name = models.CharField(max_length=50)
    cases = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    recoveries = models.IntegerField(default=0)
    date = models.DateField()
