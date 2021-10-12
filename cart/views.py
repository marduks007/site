from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import View
from cart.models import Cart
from django.contrib.auth.mixins import LoginRequiredMixin


class CartView(LoginRequiredMixin,View):
    def get(self,*args,**kwargs):
        try:
            order = Cart.objects.get(user=self.request.user,ordered=False)

        except ObjectDoesNotExist:
            messages.info(self.request,"You don't have an order")
            return render(self.request,'account/cart.html')

        context = {
            'object': order
        }
        return render(self.request,'account/cart.html',context)





