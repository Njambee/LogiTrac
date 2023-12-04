from django.contrib import admin
from django.urls import path
from LogiTrac_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('bookatruck/', views.bookatruck, name='book'),
    path('cargohandling/', views.cargohandling, name='cargohandling'),
    path('contact/', views.contact, name='contact'),
    path('get-a-quote/', views.get_quote, name='get-a-quote'),
    path('homemoving/', views.homemoving, name='homemoving'),
    path('pay/', views.pay, name='pay'),
    path('pricing/', views.pricing, name='pricing'),
    path('register/', views.register, name='register'),
    path('services/', views.services, name='services'),
    path('shipping/', views.shipping_solutions, name='shipping'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('truckingassistance/', views.truckingassistance, name='truckingassistance'),
    path('warehousing/', views.warehousing, name='warehousing'),
    ]
