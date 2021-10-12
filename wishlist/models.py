from django.db import models
from django.conf import settings
from listings.models import  WishlistItem


class Wishlist(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
   products= models.ManyToManyField(WishlistItem)
   ordered= models.BooleanField(default=False)


   def __str__(self):
       return self.user.username








