from django.urls import path
from .views import BulkProductCreateView

urlpatterns = [
    path('bulk-products/', BulkProductCreateView.as_view(), name='bulk-product-create'),
]