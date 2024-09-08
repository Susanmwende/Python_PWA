from django.db import models
from scanevent.models import ScanEvent

class RecalledDrug(models.Model):
    recalled_id = models.PositiveSmallIntegerField()
    scan_id = models.ForeignKey(ScanEvent, on_delete=models.CASCADE)   
    manufacturer_name=models.CharField(max_length=100)
    recalled_date=models.DateField()
    reason= models.CharField(max_length=100)

   
    def __str__(self):
        return f"{self.recalled_id} {self.manufacturer_name}"



