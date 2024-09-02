from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
   
    def __str__(self):
        return f"{self.user_id} {self.name}"


# Create your models here.
