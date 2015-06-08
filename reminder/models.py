from django.db import models

# Create your models here.

class Reminder(models.model):
    reminder_name = models.CharField(max_length=200)
    reminder_desc = models.CharField(max_length=1500)
    date_added = models.DateTimeField('date reminder added')
    date_reminder = models.DateTimeField('date of reminder')
    recurs = models.BooleanField('false')
    recurs_every = models.CharField(max_length=20)
