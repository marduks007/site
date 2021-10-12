from django.urls import path
from blog import views

urlpatterns = [
    path('blog',views.blog, name='blog'),
    path('blog_single',views.blog_single,name='blog_single'),
]