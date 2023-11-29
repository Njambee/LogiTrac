from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Shipment(models.Model):
    tracking_number = models.CharField(max_length=100, unique=True)
    sender_name = models.CharField(max_length=100)
    sender_address = models.CharField(max_length=255)
    recipient_name = models.CharField(max_length=100)
    recipient_address = models.CharField(max_length=255)
    shipment_description = models.TextField(max_length=300)
    shipment_status = models.CharField(max_length=255, default='In Transit')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tracking_number


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
