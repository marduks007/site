from django.urls import path
from listings import views
from listings.views import productViewDetail, shopView

urlpatterns = [
    path('shop',shopView.as_view(), name='shop'),
    path('product/<slug>',productViewDetail.as_view(), name='product'),
    path('add_to_cart/<slug>',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<slug>',views.remove_from_cart,name='remove_from_cart'),
    path('add_item_quantity/<slug>',views.add_item_quantity, name='add_item_quantity'),
    path('remove_item_quantity/<slug>',views.remove_item_quantity, name='remove_item_quantity'),
    path('add_to_wishlist/<slug>',views.add_to_wishlist,name='add_to_wishlist'),
    path('remove_from_wishlist/<slug>',views.remove_from_wishlist, name='remove_from_wishlist'),
    path('add_to_cart_from_wishlist/<slug>',views.add_to_cart_from_wishlist, name='add_to_cart_from_wishlist'),



]