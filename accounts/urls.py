from django.urls import path, include
from django.contrib.auth import views as auth_views
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

    path('reset_password/', auth_views.PasswordResetView.
         as_view(template_name="accounts/password_reset.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.
         as_view(template_name="accounts/password_reset_sent.html"), name='password_reset_done'),
    path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.
         as_view(template_name="accounts/password_reset_done.html"), name='password_reset_complete'),


]
