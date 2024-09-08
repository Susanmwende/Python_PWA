from django.urls import path
from .views import PharmacyListView
from .views import PharmacyDetailView
from .views import RecalledDrugListView
from .views import RecalledDrugDetailView
from .views import ScanEventListView
from .views import ScanEventDetailView
from .views import UserReportListView
from .views import UserReportDetailView

urlpatterns = [
    path('pharmacy/', PharmacyListView.as_view(), name='pharmacy_list_view'),
    path('pharmacy/<int:id>/', PharmacyDetailView.as_view(), name='pharmacy_detail_view'),

    
    path('recalled-drug/', RecalledDrugListView.as_view(), name='recalled_drug_list_view'),
    path('recalled-drug/<int:id>/', RecalledDrugDetailView.as_view(), name='recalled_drug_detail_view'),

    path('scan-event/', ScanEventListView.as_view(), name='scan_event_list_view'),
    path('scan-event/<int:id>/', ScanEventDetailView.as_view(), name='scan_event_detail_view'),

    path('user-report/', UserReportListView.as_view(), name='user_report_list_view'),
    path('user-report/<int:id>/', UserReportDetailView.as_view(), name='user_report_detail_view'),
]