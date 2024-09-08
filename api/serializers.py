
from rest_framework import serializers
from pharmacy.models import Pharmacy
from recalled_drug.models import RecalledDrug
from  scanevent.models import ScanEvent
from user_report.models import UserReport

class PharmacySerializer (serializers.ModelSerializer):
        class Meta:
              model= Pharmacy
              fields ="__all__"
class RecalledDrugSerializer(serializers.ModelSerializer):
      class Meta:
            model = RecalledDrug
            fields = "__all__"
class  ScanEventSerializer(serializers.ModelSerializer):
      class Meta:
            model= ScanEvent
            fields = "__all__"

class UserReportSerializer(serializers.ModelSerializer):
      class Meta:
            model = UserReport
            fields = "__all__"
