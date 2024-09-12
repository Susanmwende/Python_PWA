from django.shortcuts import render
from rest_framework.views import APIView
from pharmacy .models import Pharmacy 
from scanevent .models import ScanEvent
from recalled_drug.models import RecalledDrug
from user_report.models import UserReport
from .serializers import PharmacySerializer, RecalledDrugSerializer, ScanEventSerializer, UserReportSerializer  
from rest_framework.response import Response
from rest_framework import status

class PharmacyListView(APIView):

    def get(self, request):
        pharmacy = Pharmacy.objects.all()
        serializer = PharmacySerializer(pharmacy, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PharmacySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PharmacyDetailView(APIView):

    def get(self, request, id):
        pharmacy = Pharmacy.objects.get(id=id)
        serializer = PharmacySerializer(pharmacy)
        return Response(serializer.data)

    def put(self, request, id):
        pharmacy = Pharmacy.objects.get(id=id)
        serializer = PharmacySerializer(pharmacy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        pharmacy = Pharmacy.objects.get(id=id)
        pharmacy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


        
class RecalledDrugListView(APIView):

    def get(self, request):
        recalled_drug = RecalledDrug.objects.all()
        serializer = RecalledDrugSerializer(recalled_drug, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecalledDrugSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
class RecalledDrugDetailView(APIView):

    def get(self, request, id):
        recalled_drug = RecalledDrug.objects.get(id=id)
        serializer = RecalledDrugSerializer(recalled_drug)
        return Response(serializer.data)

    def put(self, request, id):
        recalled_drug = RecalledDrug.objects.get(id=id)
        serializer = RecalledDrugSerializer(recalled_drug, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        recalled_drug = RecalledDrug.objects.get(id=id)
        recalled_drug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class ScanEventListView(APIView):

    def get(self, request):
        scan_event = ScanEvent.objects.all()
        serializer = ScanEventSerializer(scan_event, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ScanEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ScanEventDetailView(APIView):

    def get(self, request, id):
        scan_event = ScanEvent.objects.get(id=id)
        serializer = ScanEventSerializer(scan_event)
        return Response(serializer.data)



    def put(self, request, id):
        scan_event = ScanEvent.objects.get(id=id)
        serializer = ScanEventSerializer(scan_event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        scan_event = ScanEvent.objects.get(id=id)
        scan_event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class UserReportListView(APIView):

    def get(self, request):
        user_report = UserReport.objects.all()
        serializer = UserReportSerializer(user_report, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserReportDetailView(APIView):

    def get(self, request, id):
        user_report = UserReport.objects.get(id=id)
        serializer = UserReportSerializer(user_report)
        return Response(serializer.data)

    def put(self, request, id):
        user_report = UserReport.objects.get(id=id)
        serializer = UserReportSerializer(user_report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user_report = UserReport.objects.get(id=id)
        user_report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)