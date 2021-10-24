from django.shortcuts import render
from .models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/home.html', context)


def cart(request):
    customer = request.user.customer
    order, created = customer.orders.get_or_create(completed=False)
    order_items = order.order_items.all()

    context = {
        'items': order_items,
        'order_total': order.order_total,
        'order_quantity': order.order_quantity

    }
    return render(request, 'store/cart.html', context)


def checkout(request):
    customer = request.user.customer
    order, created = customer.orders.get_or_create(completed=False)
    order_items = order.order_items.all()

    context = {
        'items': order_items,
        'order_total': order.order_total,
        'order_quantity': order.order_quantity

    }
    return render(request, 'store/checkout.html', context)