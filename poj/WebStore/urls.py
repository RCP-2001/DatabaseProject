from django.urls import path

from . import views

app_name = 'WebStore'
urlpatterns = [
    path('', views.index, name='index'),
    path('customerLi/', views.CustomerLi, name='customerLi'),
    path('customers/<int:CustomerID>/', views.detail, name='detail'),
    path('WishList/<int:WishID>/', views.WishDetails, name='WishDetails'),
    path('VenderLi/', views.VendersLi, name='VenderLi'),
    path('VenderProd/<int:VenderID>/', views.VenderDetails, name='VenderDetails'),
    path('ProductDetails/<int:ProductID>/', views.ProductDetails, name='ProductDetails'),
   # path('<int:question_id>/results/', views.results, name='results'),
   # path('<int:question_id>/vote/', views.vote, name='vote'),
   # path('specifics/<int:question_id>/', views.detail, name='detail'),
]
