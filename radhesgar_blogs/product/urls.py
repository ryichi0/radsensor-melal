from django.urls import path
from .views import ProductDetailsView, ProductExportView

app_name = 'product'

urlpatterns = [
    path('<int:product_id>/', ProductDetailsView.as_view(), name='product_details'),
    path('all/', ProductExportView.as_view(), name='all_products'),
]