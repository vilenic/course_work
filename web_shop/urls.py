from django.urls import path
from web_shop.views import views
from web_shop.views.cart import cart_view, cart_remove, cart_clean, change_quantity
from .forms import RegistrationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, logout_then_login
from web_shop.shared.utils import objects_for_nav


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>', views.item_page, name='item'),
    path('cart', cart_view, name='cart'),
    path('cart_remove', cart_remove, name='cart_remove'),
    path('cart_clean', cart_clean, name='cart_clean'),
    path('cart_change', change_quantity, name='cart_change'),
    path('create-order', views.create_order, name='create_order'),
    path('confirm-order', views.confirm_order, name='confirm_order'),



    path('register/', CreateView.as_view(
        template_name='register.html',
        form_class=RegistrationForm,
        success_url='/shop/login/',
    ), name='register'),

    path('login/', LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', logout_then_login, name='logout')
]
