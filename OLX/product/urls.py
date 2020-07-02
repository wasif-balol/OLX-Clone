from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('', productlist, name='productlist'),
    path('<slug:category_slug>', productlist, name='productlist_category'),
    path('details/<slug:product_slug>', productdetail, name='product_details')
]
