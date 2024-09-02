from django.db import models

class UserReport(models.Model):
    report_id = models.PositiveSmallIntegerField()
    town = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    pharmacy_id= models.PositiveSmallIntegerField()
    pharmacy_name=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.recalled_id} {self.manufacturer_name}"



