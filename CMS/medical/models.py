from django.db import models
from patients.models import Patient


class MedicalHistory(models.Model):
    medicalhistoryID = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    history_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Medical History for {self.patient}"

class Complaint(models.Model):
    complaintID = models.AutoField(primary_key=True)
    medical_history = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE)
    complaint_date = models.DateTimeField()
    complaint_description = models.TextField()

    def __str__(self):
         return f"Complaint for {self.medical_history.patient} on {self.complaint_date}"


class Treatment(models.Model):
    treatmentID = models.AutoField(primary_key=True)
    medical_history = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE)
    treatment_date = models.DateTimeField()
    treatment_description = models.TextField()

    def __str__(self):
        return f"Treatment for {self.medical_history.patient} on {self.treatment_date}"


class LabResult(models.Model):
    labresultID = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    lab_number = models.CharField(max_length=50)
    date_of_test = models.DateTimeField()
    test_name = models.CharField(max_length=200)
    test_result = models.TextField()
    reference_range = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Lab Result for {self.patient} on {self.date_of_test}"


class Prescription(models.Model):
    prescriptionID = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription_date = models.DateTimeField()
    medicine_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Prescription for {self.patient} on {self.prescription_date}"