from django.urls import path
from .views import UploadCSV, RetrieveData

urlpatterns = [
    path('upload-csv/', UploadCSV.as_view(), name='upload-csv'),
    path('retrieve-data/', RetrieveData.as_view(), name='retrieve-data'),
]
