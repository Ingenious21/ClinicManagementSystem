from django.db import models

class Inventory(models.Model):
    CATEGORY_CHOICES = [
    ('medication', 'medication'),
    ('lab supplies', 'lab supplies'),
    ('others', 'others')
    ]
    itemID = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200)
    item_category = models.CharField(max_length=100, choices = CATEGORY_CHOICES)
    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    reorder_level = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} ({self.item_category})"

class Service(models.Model):
    serviceID = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=200)
    service_price = models.DecimalField(max_digits=10, decimal_places = 2)
    
    def __str__(self):
        return f"{self.service_name} - ${self.service_price}"

class Medication(models.Model):
    medicationID = models.AutoField(primary_key=True)
    medication_name = models.CharField(max_length=200)
    medication_price = models.DecimalField(max_digits=10, decimal_places = 2)

    def __str__(self):
        return f"{self.medication_name} - ${self.medication_price}"