from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'title': 'Welcome to LogiTrac'})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def quote(request):
    return render(request, 'get-a-quote.html')

def pricing(request):
    return render(request, 'pricing.html')

def servicedetails(request):
    return render(request, 'service-details.html')

def services(request):
    return render(request, 'services.html')

def signup(request):
    return render(request, 'signup.html')

def bookatruck(request):
    return render(request,'bookatruck.html')