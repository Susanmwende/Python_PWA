from django.db import models

class Pharmacy(models.Model):
    pharmacy_id = models.PositiveSmallIntegerField()
    pharmacy_name= models.CharField(max_length=50)
    registration_number = models.PositiveSmallIntegerField()
    license_status= models.CharField(max_length=20)
    street = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.pharmacy_id} {self.pharmacy_name}"


