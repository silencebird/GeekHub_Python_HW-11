from django.db import models
from django.contrib.postgres.fields import ArrayField


class Askstories(models.Model):
    id = models.IntegerField(primary_key=True)
    by = models.CharField(max_length=100)
    deleted = models.NullBooleanField(null=True)
    text = models.TextField(null=True)
    dead = models.NullBooleanField(null=True)
    parent = models.CharField(max_length=100)
    descendants = models.IntegerField(null=True)
    kids = ArrayField(models.IntegerField(), null=True)
    score = models.IntegerField(null=True)
    time = models.DateTimeField()
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    url = models.CharField(max_length=200, null=True)
    parts = ArrayField(models.IntegerField(), null=True)
    poll = models.IntegerField(null=True)
