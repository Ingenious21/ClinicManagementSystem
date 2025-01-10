from django.db import models
from patients.models import Patient


class BillingInvoice(models.Model):
    invoiceID = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    invoice_date = models.DateTimeField()
    items_billed = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(blank=True, null=True)
    payment_method = models.CharField(max_length=50, default='Cash')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Invoice for {self.patient} on {self.invoice_date}"