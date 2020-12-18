from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customer/<str:pk>/', customer, name='customer'),
    path('create_order/', createOrder, name='create-order'),
    path('update_order/<str:pk>/', updateOrder, name='update-order'),
    path('delete/<str:pk>', deleteOrder, name='delete'),

]
