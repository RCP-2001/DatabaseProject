from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Customers, CustomerWishList, WishListPhone, WishListTV, Vender, Products, Service, InternetServices, PhoneServices, Phones, TVs

def index(request):

    return render(request, 'WebStore/index.html')

def CustomerLi(request):
    CustomerList = Customers.objects.order_by('-CustomerName')
    context = {
        'CustomerList': CustomerList,
    }
    return render(request, 'WebStore/Customers.html', context)

def detail(request, CustomerID):
    customers = get_object_or_404(Customers, pk=CustomerID)

    return render(request, 'WebStore/detail.html', {'customers':customers})

def WishDetails(request, WishID):
    Wish = get_object_or_404(CustomerWishList, pk=WishID)
    return render(request, 'WebStore/WishDetails.html', {'Wish':Wish} )

def VendersLi(request):
    VenderList = Vender.objects.order_by('-Name')
    context = {
        'VenderList': VenderList,
    }
    return render(request, 'WebStore/Venders.html', context)

def VenderDetails(request, VenderID):
    venders = get_object_or_404(Vender, pk=VenderID)

    return render(request, 'WebStore/VenderDetails.html', {'venders':venders})

def ProductDetails(request, ProductID):
    product = get_object_or_404(Products, pk=ProductID)

    return render(request, 'WebStore/ProductDetails.html', {'product':product})

def ServiceDetails(request, ServiceID):
    service = get_object_or_404(Service, pk=ServiceID)
    return render(request, 'WebStore/ServiceDetails.html', {'service':service})

#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)

#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)

