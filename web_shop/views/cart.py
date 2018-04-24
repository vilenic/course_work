from django.shortcuts import render
from django.http import HttpResponseRedirect
from web_shop.database.models import Item
from web_shop.shared.utils import filter_output
from cart.views import Cart
from web_shop.shared.utils import filter_output, objects_for_nav


def cart_view(request):
    if request.method == 'GET':
        cat, sub_cat, brands = objects_for_nav()
        context = {
            'categories': cat,
            'sub_categories': sub_cat,
            'brands': brands,
        }
        return render(request, 'cart.jinja2', context)


def cart_remove(request):
    if request.method == 'POST':
        item_pk = request.POST['pk']
        cart = Cart(request)
        cart.remove(pk=item_pk)
        return HttpResponseRedirect(redirect_to='/shop/cart')


def cart_clean(request):
    if request.method == 'POST':
        cart = Cart(request)
        cart.empty()
        return HttpResponseRedirect(redirect_to='/shop/cart')


def change_quantity(request):
    if request.method == 'POST':
        cart = Cart(request)
        item_pk = request.POST['pk']
        quantity = request.POST['quantity']
        cart.change_quantity(item_pk, quantity)
        return HttpResponseRedirect(redirect_to='/shop/cart')
