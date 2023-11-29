from django.urls import path, include
from LogiTrac_App import views

urlpatterns = [
    path('', include('LogiTrac_App.urls')),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('bookatruck/', views.bookatruck, name='book'),
    path('contact/', views.contact, name='contact'),
    path('get-a-quote/', views.quote, name='get-a-quote'),
    path('pricing/', views.pricing, name='pricing'),
    path('service-details/', views.servicedetails, name='service-details'),
    path('services/', views.services, name='services'),
    path('signup/', views.signup, name='signup'),

]
