from django.http import HttpResponse
from requests.auth import HTTPBasicAuth
from django.shortcuts import render, redirect
from LogiTrac_App.credentials import LipanaMpesaPpassword, MpesaAccessToken
from LogiTrac_App.forms import QuoteForm
from LogiTrac_App.models import Member, ShippingInfo
import requests
import json


# Create your views here.

def register(request):
    if request.method == 'POST':
        member = Member(fullname=request.POST['fullname'], username=request.POST['username'],
                        email=request.POST['email'], password=request.POST['password'])
        member.save()
        return redirect('index/')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def index(request):
    if request.method == 'POST':
        if Member.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            member = Member.objects.get(email=request.POST['email'], password=request.POST['password'])
            return render(request, 'index.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def get_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            return render(request, 'thank_you.html')
    else:
        form = QuoteForm()

    return render(request, 'get-a-quote.html', {'form': form})


def pricing(request):
    return render(request, 'pricing.html')


def services(request):
    return render(request, 'services.html')


def bookatruck(request):
    return render(request, 'bookatruck.html')


def cargohandling(request):
    return render(request, 'cargohandling.html')


def token(request):
    consumer_key = 'nYosK08GYU3AvQ2pMdafWHueGDjGGvHT'
    consumer_secret = 'r6j4dkX0rfzMlHyy'
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_url, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token": validated_mpesa_access_token})


def pay(request):
    return render(request, 'pay.html')


def shipping(request):
    if request.method == 'POST':
        cargo_details = request.POST.get('cargo_details')
        pickup_address = request.POST.get('pickup_address')
        delivery_address = request.POST.get('delivery_address')

        ShippingInfo.objects.create(
            cargo_details=cargo_details,
            pickup_address=pickup_address,
            delivery_address=delivery_address
        )

    return render(request, 'shippingsolutions.html')


def homemoving(request):
    return render(request, 'homemovingservices.html')


def warehousing(request):
    return render(request, 'warehousing.html')


def truckingassistance(request):
    return render(request, 'truckingassistance.html')


def stk(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "LogiTrac",
            "TransactionDesc": "Transportation costs"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse(response)
