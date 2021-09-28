from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.
def home(request):
    list = range(0, 3)
    context = {
        'list': list
    }
    return render(request, 'store/home.html', context)


def cart(request):
    return render(request, 'store/cart.html')


def checkout(request):
    return render(request, 'store/checkout.html')