from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', reg_page, name='register'),

    path('', home, name='home'),
    path('user/', user_page, name="user-page"),
    path('account/', account_settings, name='account'),
    path('products/', products, name='products'),
    path('customer/<str:pk>/', customer, name='customer'),

    path('create_order/', createOrder, name='create-order'),
    path('update_order/<str:pk>/', updateOrder, name='update-order'),
    path('delete/<str:pk>', deleteOrder, name='delete'),

]
