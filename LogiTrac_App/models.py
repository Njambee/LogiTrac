from django.db import models


class Member(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class CargoHandling(models.Model):
    cargo_details = models.TextField()
    pickup_address = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=100)

    def __str__(self):
        return "Cargo - ID: {self.id}"


class HomeMoving(models.Model):
    belongings_details = models.TextField()
    pickup_address = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=100)

    def __str__(self):
        return "Home Moving - ID: {self.id}"


class WareHousing(models.Model):
    goods_details = models.TextField()
    pickup_address = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=100)

    def __str__(self):
        return "Warehousing - ID: {self.id}"


class TruckingAssistance(models.Model):
    cargo_details = models.TextField()
    pickup_address = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=100)

    def __str__(self):
        return "Trucking Assistance - ID: {self.id}"


class ShippingInfo(models.Model):
    cargo_details = models.TextField()
    pickup_address = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=100)

    def __str__(self):
        return "Shipping Information - ID: {self.id}"


class MpesaPayment(models.Model):
    transaction_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "M-Pesa Payment - {self.transaction_id}"


# models.py

class Quote(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    shipment_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
