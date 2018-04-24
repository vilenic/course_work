from django.contrib import admin
from web_shop.database.models import Item, Category, SubCategory, Manufacturer
from web_shop.database.order import OrderItem, Order, Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'full', )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'delivery_address',
        'date_added',
        'delivered',
    )


class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'item',
        'order',
        'id',
    )


admin.site.register(Item)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Manufacturer)
admin.site.register(Address, AddressAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

