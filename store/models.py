from django.db import models
from users.models import Customer


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(default='product.png')
    digital = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='orders', null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)

    @property
    def order_total(self):
        total = sum([item.item_total for item in self.order_items.all()])
        return total

    @property
    def order_quantity(self):
        quantity = sum([item.quantity for item in self.order_items.all()])
        return quantity


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, related_name='order_items', null=True)

    @property
    def item_total(self):
        return self.product.price * self.quantity


class ShippingAddress(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
