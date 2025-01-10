from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    patientID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_number = models.CharField(max_length=15)

    @property
    def age(self):
        today = timezone.now().date()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - PatientID: {self.patientID}"
    




class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Administrator', 'Administrator'),
        ('Registrar', 'Registrar'),
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Registrar')

    def __str__(self):
        return self.username
