from django.db import models

class Pharmacy(models.Model):
    pharmacy_id = models.PositiveSmallIntegerField()
    pharmacy_name= models.CharField(max_length=50)
    registration_number = models.PositiveSmallIntegerField()
    license_status= models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    town = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.pharmacy_id} {self.pharmacy_name}"


# Create your models here.
