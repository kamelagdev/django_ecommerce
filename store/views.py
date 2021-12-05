from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from .models import Product
import json


# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/home.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = customer.orders.get_or_create(completed=False)
        order_items = order.order_items.all()
    else:
        order_items = []
        print('ok')
        order = {
            'order_total': 0,
            'order_quantity': 0,
        }

    context = {
        'items': order_items,
        'order': order,
    }
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = customer.orders.get_or_create(completed=False)
        order_items = order.order_items.all()

        order = {
            'order_total': order.order_total,
            'order_quantity': order.order_quantity,
        }
    else:
        order_items = []
        print('ok')
        order = {
            'order_total': 0,
            'order_quantity': 0,
        }

    context = {
        'items': order_items,
        'order_total': order['order_total'],
        'order_quantity': order['order_quantity']

    }
    return render(request, 'store/checkout.html', context)


def update_cart(request):
    if request.user.is_authenticated:
        print('auth')
        data = json.loads(request.body)
        product_id = data['productId']
        action = data['action']
        product = Product.objects.get(id=product_id)
        customer = request.user.customer
        order, created = customer.orders.get_or_create(completed=False)
        item, created = order.order_items.get_or_create(product=product)

        if action == 'add':
            item.quantity += 1
            messages.success(request, 'Item added successfully')
        elif action == 'remove':
            item.quantity -= 1
        item.save()

        if item.quantity <= 0:
            item.delete()
            messages.info(request, 'Item removed!')

    else:
        print('not auth')
    return JsonResponse('cart updated ', safe=False)
