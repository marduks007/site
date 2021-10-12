
from django.contrib import messages
from django.http import request
from django.shortcuts import  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import ListView, DetailView
from cart.models import Cart
from wishlist.models import Wishlist

from .models import Listing, OrderItem, WishlistItem


class shopView(ListView):
    model = Listing
    template_name = 'listings/shop.html'
    paginate_by = 4


    def get_queryset(self):
        all_qs = super().get_queryset().all()


        if 'vegetables' in self.request.GET:
            qs = super().get_queryset().filter(category='V')
            return qs
        if 'fruits' in self.request.GET:
            qs = super().get_queryset().filter(category='F')
            return qs
        if 'juice' in self.request.GET:
            qs = super().get_queryset().filter(category='J')
            return qs
        if 'poultry' in self.request.GET:
            qs = super().get_queryset().filter(category='P')
            return qs
        if 'all' in self.request.GET:
            return all_qs

        return all_qs

class productViewDetail(DetailView):
    model =  Listing
    template_name = 'listings/product-single.html'


@login_required()
def add_to_cart(request,slug):

        item = get_object_or_404(Listing, slug=slug)

        #creating an order item object
        order_item,created = OrderItem.objects.get_or_create(item=item,user=request.user,ordered=False)

        #creating a queryset order that gets a cart object of user and unordered item
        order_qs = Cart.objects.filter(user=request.user, ordered=False)
        # check if a queryset order of requested user  exist
        if order_qs.exists():
            order = order_qs[0]

            # check if the order item is in the cart/queryset
            if order.products.filter(item__slug=item.slug).exists():

                messages.info(request,'Item  already in the cart')
                return redirect('shop')

            else:
                order.products.add(order_item)
                messages.success(request,'Item is added to the cart')
                return redirect('shop')


        else:

            ordered_date = timezone.now()
            # create an order to the cart
            order = Cart.objects.create(user=request.user,ordered_date = ordered_date)
            order.products.add(order_item)
            messages.success(request,'Item is added to the cart')
            

        return redirect('product' , slug=slug)

@login_required()
def remove_from_cart(request,slug):

    item = get_object_or_404(Listing, slug=slug)
    order_qs = Cart.objects.filter(user=request.user, ordered=False)
    # check if an order exist
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the cart
        if order.products.filter(item__slug=item.slug).exists():
            order_item=OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            #remove  order from cart
            order.products.remove(order_item)
            #delete orderItem
            order_item.delete()
            messages.success(request, 'Item was removed from cart')
            return redirect('cart')
        else:
            #add a message that says the item is not in the cart
            messages.error(request, 'Item is not in the cart')
            return redirect('product', slug=slug)
    else:
        #adding a message saying that the user has no existing order
        messages.error(request,'No existing order')
    return redirect('product', slug=slug)

def add_item_quantity(request,slug):
    item = get_object_or_404(Listing,slug=slug)

    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)

    # creating a queryset that filter a cart object of user and unordered item
    order_qs = Cart.objects.filter(user=request.user, ordered=False)
    # check if an queryset  of requested user  exist
    if order_qs.exists():
        order = order_qs[0]

        # check if the order item is in the cart/queryset
        if order.products.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.success(request, 'Item  quantity  updated')
            return redirect('cart')

def remove_item_quantity(request,slug):
    item = get_object_or_404(Listing,slug=slug)

    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)

    # creating a queryset that filter a cart object of user and unordered item
    order_qs = Cart.objects.filter(user=request.user, ordered=False)
    # check if an queryset  of requested user  exist
    if order_qs.exists():
        order = order_qs[0]

        # check if the order item is in the cart/queryset
        if order.products.filter(item__slug=item.slug).exists():
            order_item.quantity -= 1
            order_item.save()
            messages.success(request, 'Item  quantity reduced')
            return redirect('cart')



@login_required()
def add_to_wishlist(request,slug):
    item = get_object_or_404(Listing,slug=slug)
    #create a wishlistItem object
    wishlist_item, created = WishlistItem.objects.get_or_create(item=item, user=request.user, ordered=False)

    wishlist_qs= Wishlist.objects.filter(user=request.user,ordered=False)
    if wishlist_qs.exists():
        wishlist=wishlist_qs[0]
        #check if item is in wishlist
        if wishlist.products.filter(item__slug= item.slug).exists():
            messages.error(request,'Item already on your wishlist')
            return redirect('shop')
        else:
            wishlist.products.add(wishlist_item)
            messages.success(request, 'Item is added to your wishlist')
            return redirect('shop')
    else:
        wishlist=Wishlist.objects.create(user=request.user)
        wishlist.products.add(wishlist_item)
        messages.success(request,'Item added to your wishlist')
    return redirect('shop')


@login_required()
def remove_from_wishlist(request,slug):

    item = get_object_or_404(Listing, slug=slug)
    wishlist_qs = Wishlist.objects.filter(user=request.user, ordered=False)
    # check if a wishlist exist
    if wishlist_qs.exists():
        wishlist = wishlist_qs[0]
        # check if the wishlist item is in the wishlist
        if wishlist.products.filter(item__slug=item.slug).exists():
            wishlist_item=WishlistItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            wishlist.products.remove(wishlist_item)
            wishlist_item.delete()
            messages.success(request, 'Item was removed from your wishlist')
            return redirect('wishlist')
        else:
            #add a message that says the item is not in the cart
            messages.error(request, 'Item is not in your wishlist')
            return redirect('wishlist')
    else:
        #adding a message saying that the user has a wishlist
        messages.error(request,'No existing wishlist')
    return redirect('wishlist')

def add_to_cart_from_wishlist(request,slug):
    item = get_object_or_404(Listing, slug=slug)

    # creating an order item object
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)


    # creating a queryset that gets a cart object of user and unordered item
    order_qs = Cart.objects.filter(user=request.user, ordered=False)
    # check if an queryset  of requested user  exist
    if order_qs.exists():
        order = order_qs[0]

        # check if the order item is in the cart/queryset
        if order.products.filter(item__slug=item.slug).exists():

            messages.error(request, 'Item  already in the cart')
            return redirect('wishlist')

        else:
            order.products.add(order_item)
            messages.success(request, 'Item is added to the cart')
            return redirect('wishlist')


    else:

        ordered_date = timezone.now()
        # create an order to the cart
        order = Cart.objects.create(user=request.user, ordered_date=ordered_date)
        order.products.add(order_item)
        messages.success(request, 'Item is added to the cart')

    return redirect('wishlist')







