from django.shortcuts import render

# Create your views here.
class UserReport(models.Model):
    report_id = models.PositiveSmallIntegerField()
    town= models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    pharmacy_id = models.PositiveSmallIntegerField()
    pharmacy_name= models.CharField(max_length=50)
   
    def __str__(self):
        return f"{self.report_id} {self.town}"



