from django.db import models


class Appointment(models.Model):
    patient = models.CharField(max_length=120)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    comments = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.patient