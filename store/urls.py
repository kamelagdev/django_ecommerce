from django.urls import path
from .views import home, cart, checkout, update_cart

urlpatterns = [
    path('', home, name='home'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update-cart/', update_cart, name="update-cart")
]