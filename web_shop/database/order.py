import datetime
from django.db import models
from .models import Item
from django.contrib.auth.models import User
from django.utils import timezone


class Address(models.Model):
    full = models.CharField(max_length=150)

    def __str__(self):
        return self.full


class Order(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )
    delivery_address = models.ForeignKey(
        Address,
        on_delete=models.DO_NOTHING
    )
    date_added = models.DateTimeField(default=timezone.now)
    delivered = models.BooleanField(default=False)
    date_delivered = models.DateTimeField(blank=True, null=True)
    order_items = models.ManyToManyField(
        'OrderItem',
        related_name='items',
    )

    def mark_delivered(self, commit=True):
        self.delivered = True
        self.date_delivered = timezone.now()
        if commit:
            self.save()

    def __str__(self):
        return 'Order #{}'.format(self.pk)


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return 'Item: {}, Quantity: {}'.format(self.item, self.quantity)
