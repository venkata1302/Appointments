from django.db import models

class Appointment(models.Model):
    date_time = models.DateTimeField()
    description = models.CharField(max_length = 20)

