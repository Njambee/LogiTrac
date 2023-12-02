from django import forms
from LogiTrac_App.models import ShippingInfo, MpesaPayment, CargoHandling, WareHousing, HomeMoving, Quote


class ShippingInfoForm(forms.ModelForm):
    class Meta:
        model = ShippingInfo
        fields = ['cargo_details', 'pickup_address', 'delivery_address']


class WareHousingForm(forms.ModelForm):
    class Meta:
        model = WareHousing
        fields = ['goods_details', 'pickup_address', 'delivery_address']


class HomeMovingForm(forms.ModelForm):
    class Meta:
        model = HomeMoving
        fields = ['belongings_details', 'pickup_address', 'delivery_address']


class CargoHandlingForm(forms.ModelForm):
    class Meta:
        model = CargoHandling
        fields = ['cargo_details', 'pickup_address', 'delivery_address']


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['name', 'email', 'shipment_details']


class MpesaPaymentForm(forms.ModelForm):
    class Meta:
        model = MpesaPayment
        fields = ['phone_number', 'amount']
