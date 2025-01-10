from django.db import models
from patients.models import Patient
from django.conf import settings

class Appointment(models.Model):
    APPOINTMENT_TYPE_CHOICES = [
    ('Medical', 'Medical'),
    ('Eye', 'Eye')
    ]
    appointmentID = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_of_visit = models.DateTimeField()
    appointment_type = models.CharField(max_length=50, choices = APPOINTMENT_TYPE_CHOICES)
    attending_doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Appointment for {self.patient} on {self.date_of_visit}"