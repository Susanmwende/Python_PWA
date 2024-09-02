from django.db import models

class Location(models.Model):
    location= models.CharField(max_length=50)
    pharmacy_id = models.PositiveSmallIntegerField()
    latitude= models.PositiveSmallIntegerField()
    longitude = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.location} {self.pharmacy_id}"


