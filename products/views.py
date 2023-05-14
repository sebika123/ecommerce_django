from django.shortcuts import render,HttpResponse
from products.models import Product
# Create your views here.
def products(request):
    #product=Product.objects.all()
    #return render(request,'products.html',{'products':product})
    return HttpResponse('helloworld')