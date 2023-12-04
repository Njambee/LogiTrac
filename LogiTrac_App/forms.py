from django import forms
from LogiTrac_App.models import ShippingInfo, MpesaPayment, CargoHandling, WareHousing, HomeMoving, Quote, Contact, \
    TruckBooking, TruckingAssistance


class ShippingInfoForm(forms.ModelForm):
    class Meta:
        model = ShippingInfo
        fields = ['name', 'contact', 'cargo_details', 'pickup_address', 'delivery_address']


class WareHousingForm(forms.ModelForm):
    class Meta:
        model = WareHousing
        fields = ['name', 'contact', 'goods_details', 'pickup_address', 'delivery_address']


class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class HomeMovingForm(forms.ModelForm):
    class Meta:
        model = HomeMoving
        fields = ['name', 'contact', 'belongings_details', 'pickup_address', 'delivery_address']


class CargoHandlingForm(forms.ModelForm):
    class Meta:
        model = CargoHandling
        fields = ['name', 'contact', 'cargo_details', 'pickup_address', 'delivery_address']


class TruckingAssistanceForm(forms.ModelForm):
    class Meta:
        model = TruckingAssistance
        fields = ['name', 'contact', 'cargo_details', 'pickup_address', 'delivery_address']


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['name', 'email', 'shipment_details']


class MpesaPaymentForm(forms.ModelForm):
    class Meta:
        model = MpesaPayment
        fields = ['phone_number', 'amount']


class TruckBookingForm(forms.ModelForm):
    class Meta:
        model = TruckBooking
        fields = ['sender_name', 'sender_address', 'receiver_name', 'receiver_address', 'shipment_details',
                  'pickup_time', 'dropoff_time']
        widgets = {
            'pickup_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'dropoff_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
