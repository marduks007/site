from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from listings.models import Listing

class HomeView(ListView):
     model = Listing
     template_name= 'pages/index.html'
     paginate_by = 4

def about(request):
     return render(request,'pages/about.html')