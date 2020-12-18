from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
from .forms import *


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
    orders = customers.order_set.all()
    orders_count = orders.count()
    context = {'customer': customers, 'order': orders, 'orders_count': orders_count}
    return render(request, 'accounts/customer.html', context)


def createOrder(request):
    forms = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': forms}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}

    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    order.is_delete = True
    order.save()
    return redirect('/')
