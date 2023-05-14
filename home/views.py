from django.shortcuts import render,HttpResponse
from . import models
from products.models import Products
# Create your views here.
def home(request):
    #latestItems = Items.objects.order_by('-id')[:2]
    sliders = Products.objects.filter(section__title='Slider')
    return render(request, 'home.html', {'sliders': sliders})



