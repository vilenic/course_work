from django.shortcuts import render
from easycart import BaseCart
from web_shop.database.models import Item


class Cart(BaseCart):

    def get_queryset(self, pks):
        return Item.objects.filter(pk__in=pks)
