from django.http import HttpResponse
from requests.auth import HTTPBasicAuth
from django.shortcuts import render, redirect
from LogiTrac_App.credentials import LipanaMpesaPpassword, MpesaAccessToken
from LogiTrac_App.forms import QuoteForm, TruckBookingForm, ShippingInfoForm, HomeMovingForm, WareHousingForm, \
    TruckingAssistanceForm, CargoHandlingForm
from LogiTrac_App.models import Member, TruckBooking
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
    if request.method == 'POST':
        form = TruckBookingForm(request.POST)  # If you have a form, use it here
        if form.is_valid():
            # Create an instance of TruckBooking model and save the data
            booking = TruckBooking(
                sender_name=form.cleaned_data['senderName'],
                sender_address=form.cleaned_data['senderAddress'],
                receiver_name=form.cleaned_data['receiverName'],
                receiver_address=form.cleaned_data['receiverAddress'],
                shipment_details=form.cleaned_data['shipmentDetails'],
                pickup_time=form.cleaned_data['pickupTime'],
                dropoff_time=form.cleaned_data['dropoffTime']
            )
            booking.save()
            return redirect('thank_you.html')

    else:
        form = TruckBookingForm()

    return render(request, 'bookatruck.html', {'form': form})

def cargohandling(request):
    if request.method == 'POST':
        form = CargoHandlingForm(request.POST)
        if form.is_valid():
            return render(request, 'thank_you.html')
    else:
        form = CargoHandlingForm()

    return render(request, 'cargohandling.html', {'form': form})

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


def shipping_solutions(request):
    if request.method == 'POST':
        form = ShippingInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')
    else:
        form = ShippingInfoForm()

    return render(request, 'shipping_solutions.html', {'form': form})


def homemoving(request):
    if request.method == 'POST':
        form = HomeMovingForm(request.POST)
        if form.is_valid():
            return render(request, 'thank_you.html')
    else:
        form = HomeMovingForm()

    return render(request, 'homemovingservices.html', {'form': form})


def warehousing(request):
    if request.method == 'POST':
        form = WareHousingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')
    else:
        form = WareHousingForm()

    return render(request, 'warehousing.html', {'form': form})


def truckingassistance(request):
    if request.method == 'POST':
        form = TruckingAssistanceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')
    else:
        form = TruckingAssistanceForm()

    return render(request, 'truckingassistance.html', {'form': form})


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


def thank_you(request):
    return render(request, 'thank_you.html')
