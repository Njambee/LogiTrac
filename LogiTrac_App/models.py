from django.db import models


class Member(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class CargoHandling(models.Model):
    name = models.CharField(max_length=100, default='')
    contact = models.CharField(max_length=20, default='')
    cargo_details = models.TextField()
    pickup_address = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=100)


class HomeMoving(models.Model):
    name = models.CharField(max_length=100, default='')
    contact = models.CharField(max_length=20, default='')
    belongings_details = models.TextField()
    pickup_address = models.CharField(max_length=200)
    delivery_address = models.CharField(max_length=200)


class WareHousing(models.Model):
    name = models.CharField(max_length=100, default='')
    contact = models.CharField(max_length=20, default='')
    goods_details = models.TextField()
    pickup_address = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=100)


class TruckingAssistance(models.Model):
    name = models.CharField(max_length=100, default='')
    contact = models.CharField(max_length=20, default='')
    cargo_details = models.TextField()
    pickup_address = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=100)


class ShippingInfo(models.Model):
    name = models.CharField(max_length=100, default='')
    contact = models.CharField(max_length=20, default='')
    cargo_details = models.TextField()
    pickup_address = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=100)


class MpesaPayment(models.Model):
    transaction_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)


class Quote(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    shipment_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class TruckBooking(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_address = models.TextField()
    receiver_name = models.CharField(max_length=100)
    receiver_address = models.TextField()
    shipment_details = models.TextField()
    pickup_time = models.DateTimeField()
    dropoff_time = models.DateTimeField()

    def __str__(self):
        return "Truck Booking - {self.sender_name} to {self.receiver_name}"
