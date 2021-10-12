from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

CATEGORY_CHOICES = (
    ('V','vegetables'),
    ('F','fruits'),
    ('P','poultry'),
    ('J','juice'),
)

MEASUREMENTS = (
    ('Kg','kg'),
    ('G','g'),
    ('Ltr','ltr'),
    ('None',''),
)


class Listing(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField(default=0,null=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    rating = models.IntegerField(blank=True,null=True)
    sold = models.IntegerField(blank=True,null=True)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=20)
    slug = models.SlugField( unique =True,default= 'product-')
    ordered = models.BooleanField(default=False)
    measure= models.CharField(choices=MEASUREMENTS,blank=True,max_length=20)




    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product' , kwargs={
            'slug':self.slug
        })

    def get_add_to_cart_url(self):
        return reverse('add_to_cart' ,kwargs={
            'slug':self.slug
        })
    def get_remove_from_cart_url(self):
        return reverse('remove_from_cart', kwargs= {
            'slug': self.slug
        })
    def get_add_to_wishlist_url(self):
        return reverse('add_to_wishlist', kwargs={
            'slug':self.slug
        })

    def get_remove_from_wishlist(self):
        return reverse('remove_from_wishlist', kwargs={
            'slug':self.slug
        })

    def get_add_to_cart_from_wishlist(self):
        return reverse('add_to_cart_from_wishlist', kwargs={
            'slug': self.slug
        })

    def get_add_item_quantity_url(self):
        return reverse('add_item_quantity' , kwargs={
            'slug':self.slug
        })

    def get_remove_item_quantity_url(self):
        return reverse('remove_item_quantity' , kwargs={
            'slug':self.slug
        })



class OrderItem(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
        ordered = models.BooleanField(default=False)
        item = models.ForeignKey(Listing,on_delete=models.CASCADE, null=True)
        quantity = models.IntegerField(default=1)


        def __str__(self):
            return f"{self.quantity} quantity of {self.item}"

        def get_total_item_price(self):
            return self.quantity * self.item.price


        def get_total_discount_price(self):
            return self.quantity * self.item.discount_price

        def get_total_price(self):
            if self.item.discount_price:
                return self.get_total_item_price() - self.get_total_discount_price()
            return self.get_total_item_price()





class WishlistItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    ordered = models.BooleanField(default=False)
    item= models.ForeignKey(Listing,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.item.product_name