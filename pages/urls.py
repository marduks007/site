from django.urls import path
from .views import HomeView

from pages import views

urlpatterns = [
    path('',HomeView.as_view(), name='index'),
    path('about',views.about, name='about')
]