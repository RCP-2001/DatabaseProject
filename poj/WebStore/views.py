from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
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

def AddCustomer(request):
    CustomerList = Customers.objects.order_by('-CustomerName')
    context = {
        'CustomerList': CustomerList,
        'error_message': "Select Router"
    }
    name = request.POST['CusName']

    try:
        router = request.POST["router"]
    except(KeyError):
        return render(request, 'WebStore/Customers.html', context)
    else:
        Cust = Customers(CustomerName = name, OwnsRouter=router)
        Cust.save()
        return HttpResponseRedirect(reverse('WebStore:customerLi'))

def NewWishList(request, CID):
    customers = get_object_or_404(Customers, pk=CID)
    wType = request.POST['Type']
    wAmmountOfItem = request.POST['AmmountOfItem']
    wPrice = request.POST['Price']
    w = CustomerWishList(CustomerID=customers, Type=wType, AmmountOfItem = wAmmountOfItem, Price = wPrice)
    w.save()
    return HttpResponseRedirect(reverse('WebStore:detail', args=(CID,)))

def AddVender(request):
    VenderList = Vender.objects.order_by('Name')
    context = {
        'VenderList': VenderList,
        'error_message': "Somethign went wrong"
    }
    name = request.POST['VenName']
    V = Vender(Name=name)
    V.save()

    return HttpResponseRedirect(reverse('WebStore:VenderLi'))

def AddProducts(request, VID):
    venders = get_object_or_404(Vender, pk=VID)
    wDesc = request.POST['Description']
    wPrice = request.POST['Price']
    wDeliveryCost = request.POST['DeliveryCost']
    wDeliveryLength = request.POST['DeliveryLength']
    wType = request.POST['Type']

    p = Products(Description = wDesc, Price = wPrice, DeliveryCost = wDeliveryCost, DeliveryLength = wDeliveryLength, Type = wType, VenderID=venders)
    p.save()
    return HttpResponseRedirect(reverse('WebStore:VenderDetails', args=(VID,)))

def UpdatePhone(request, PID):
    Prod = get_object_or_404(Products, pk = PID)

    wBrand = request.POST['Brand']
    wQuality = request.POST['Quality']
    wGeneration = request.POST['Generation']
    wCameraQuality = request.POST['CameraQuality']

    p = Phones(ProductID = Prod, Brand = wBrand, Quality = wQuality, Generation = wGeneration, CameraQuality = wCameraQuality)
    p.save()

    return HttpResponseRedirect(reverse('WebStore:ProductDetails', args=(PID,)))


def UpdateTVs(request, PID):
    Prod = get_object_or_404(Products, pk = PID)

    wBrand = request.POST['Brand']
    wHertz = request.POST['Hertz']
    wScreenType = request.POST['ScreenType']
    wScreenSize = request.POST['ScreenSize']

    p = TVs(ProductID = Prod, Brand = wBrand, Hertz = wHertz, ScreenSize = wScreenSize, ScreenType = wScreenType)
    p.save()

    return HttpResponseRedirect(reverse('WebStore:ProductDetails', args=(PID,)))

