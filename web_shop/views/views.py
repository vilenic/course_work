from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from web_shop.database.models import Item
from web_shop.database.order import OrderItem, Order
from web_shop.shared.utils import filter_output, objects_for_nav
from cart.views import Cart
from django.core.paginator import Paginator
from web_shop.forms import DeliveryForm
from django.db import transaction
from django.contrib.auth.models import User


def index(request):

    params = filter_output(request)

    if request.method == 'GET':
        items = Item.objects.filter(
            manufacturer__name__icontains=params['manufacturer']
        ).filter(
            category__name__icontains=params['category']
        ).filter(
            sub_category__name__icontains=params['sub_category']
        ).order_by('manufacturer__name')

        paginator = Paginator(items, params['per_page'])
        item_list = paginator.get_page(params['page'])

        cat, sub_cat, brands = objects_for_nav()
        query_length = len(item_list)
        if query_length <= 2:
            query_split = 1
        elif query_length % 2 == 0:
            query_split = query_length // 2
        else:
            query_split = (query_length // 2) + 1

        context = {
            'query_length': query_length,
            'item_list_paginator': item_list,
            'items_left': item_list[:query_split],
            'items_right': item_list[query_split:],
            'categories': cat,
            'sub_categories': sub_cat,
            'brands': brands,
            'cur_category': params['category'],
            'cur_sub_category': params['sub_category'],
            'cur_brand': params['manufacturer'],
        }
        return render(request, 'index.jinja2', context)


def item_page(request, item_id):
    cat, sub_cat, brands = objects_for_nav()
    if request.method == 'GET':
        _item = Item.objects.get(pk=item_id)
        print(_item.category)
        context = {
            'item': _item,
            'categories': cat,
            'sub_categories': sub_cat,
            'brands': brands,
            'cur_category': _item.category,
            'cur_sub_category': _item.sub_category,
            'cur_brand': _item.manufacturer,
        }
        return render(request, 'item.jinja2', context)

    elif request.method == 'POST':
        cat, sub_cat, brands = objects_for_nav()
        pk = request.POST['pk']
        cart = Cart(request)
        cart.add(pk=pk)
        context = {
            'categories': cat,
            'sub_categories': sub_cat,
            'brands': brands,
        }
        return render(request, 'cart.jinja2', context)


def create_order(request):
    cat, sub_cat, brands = objects_for_nav()
    context = {
        'delivery_form': DeliveryForm(),
        'categories': cat,
        'sub_categories': sub_cat,
        'brands': brands,
    }
    return render(request, 'confirm_order.html', context)


def confirm_order(request):
    cat, sub_cat, brands = objects_for_nav()
    if request.method == 'POST':
        address_form = DeliveryForm(request.POST)
        user = User.objects.get(pk=request.POST['user'])
        cart = Cart(request)
        if address_form.is_valid():
            with transaction.atomic():
                address = address_form.save()
                order = Order(
                    delivery_address=address,
                    user=user
                )
                order.save()
                item_list = cart.list_items()
                if not item_list:
                    return HttpResponseRedirect('/shop/cart')
                else:
                    for item in item_list:
                        ordered_item = OrderItem(
                            item=Item.objects.get(pk=item.obj.pk),
                            order=order,
                            quantity=item.quantity
                        )
                        ordered_item.save()
                        order.order_items.add(ordered_item.pk)
                    cart.empty()
                    context = {
                        'order_id': order.pk,
                        'categories': cat,
                        'sub_categories': sub_cat,
                        'brands': brands,
                    }
                    return render(request, 'order_success.html', context)
        else:
            # todo template
            return HttpResponse(content='Invalid address')

    return HttpResponse(content='hello')
