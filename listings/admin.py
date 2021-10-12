from django.contrib import admin

from cart.models import Cart
from .models import Listing, OrderItem


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','is_published','price','category')
    list_display_links = ('id','product_name')
    list_filter = ('id','product_name','category')
    list_editable = ('is_published',)
    list_per_page = 25


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Listing,ListingAdmin)
admin.site.register(OrderItem)
admin.site.register(Cart,OrderAdmin)



