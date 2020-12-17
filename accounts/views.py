from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_ordered = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='pending').count()

    context = {'orders': orders, 'customers': customers, 'total_ordered': total_ordered, 'delivered': delivered,
               'pending': pending}
    return render(request, 'accounts/dashbord.html', context)


def products(request):
    product = Product.objects.all()
    context = {'pd': product}
    return render(request, 'accounts/product.html', context)


def customer(request, pk):
    customers = Customer.objects.get(id=pk)
    orders = Customer.order_set.all()
    context = {'customer': customers, 'order': orders}
    return render(request, 'accounts/customer.html', context)
