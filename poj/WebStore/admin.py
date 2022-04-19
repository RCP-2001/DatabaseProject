from django.contrib import admin

from .models import Customers, CustomerWishList

admin.site.register(Customers)
admin.site.register(CustomerWishList)