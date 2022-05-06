from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Customers, CustomerWishList

def index(request):
    CustomerList = Customers.objects.order_by('-CustomerName')
    context = {
        'CustomerList': CustomerList,
    }
    return render(request, 'WebStore/index.html', context)

def detail(request, CustomerID):
    customers = get_object_or_404(Customers, pk=CustomerID)

    return render(request, 'WebStore/detail.html', {'customers':customers})

#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)

#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)

