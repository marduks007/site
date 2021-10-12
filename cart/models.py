from django.conf import settings
from django.db import models

from checkout.models import BillingAddress
from listings.models import OrderItem




class Cart(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateField()
    ordered = models.BooleanField(default=False)
    delivery_price = models.FloatField(default=2000)
    billing_address = models.ForeignKey('checkout.BillingAddress', related_name='billing_address',on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.user


    def get_subtotal_price(self):
        total = 0
        for order_item in self.products.all():
            total += order_item.get_total_price()
        return total


    def get_final_total_price(self):
       final_total = self.get_subtotal_price() + self.delivery_price
       return final_total








