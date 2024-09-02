from django.db import models

class RecalledDrug(models.Model):
    recalled_id = models.PositiveSmallIntegerField()
    manufacturer_name = models.CharField(max_length=100)
    drug_name = models.CharField(max_length=30)
    batch_number = models.CharField(max_length=30)
    pharmacy_id= models.PositiveSmallIntegerField()
    recalled_date=models.DateField()
    reason_for_recall= models.CharField(max_length=50)
   
    def __str__(self):
        return f"{self.recalled_id} {self.manufacturer_name}"



