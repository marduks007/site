from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View
from .models import Wishlist




class WishlistView(LoginRequiredMixin,View):
    def get(self,*args,**kwargs):
        try:
            wishlist=Wishlist.objects.get(user=self.request.user)
        except ObjectDoesNotExist:
            messages.info(self.request, "You don't have an item in your wishlist")
            return render(self.request, 'account/wishlist.html')

        context = {
                'object': wishlist
            }

        return render(self.request, 'account/wishlist.html', context)











