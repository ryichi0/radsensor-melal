from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('all/', ProductExportView.as_view(), name='all_products'),
    path('<str:slug>/', ProductDetailsView.as_view(), name='product_details'),
    path('datasheet-download/all/', DownloadExportView.as_view(), name='all_datasheets'),
]