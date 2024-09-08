from django.db import models
from recalled_drug.models import  RecalledDrug
from pharmacy.models import Pharmacy

class UserReport(models.Model):
    report_id = models.PositiveSmallIntegerField()    
    pharmacy_id = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    recalled_id = models.ForeignKey(RecalledDrug, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.report_id} {self.pharmacy_id}"



