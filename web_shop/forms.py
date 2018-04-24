from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from web_shop.database.order import Order, Address


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]


class OrderCreationForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'delivery_address',
        ]


class DeliveryForm(ModelForm):
    class Meta:
        model = Address
        fields = [
            'full',
        ]
