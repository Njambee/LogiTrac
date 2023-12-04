from django.contrib import admin
from LogiTrac_App.models import Member, CargoHandling, MpesaPayment, HomeMoving, TruckingAssistance, ShippingInfo, WareHousing, \
    Quote

# Register your models here.
admin.site.register(Member)
admin.site.register(Quote)
admin.site.register(CargoHandling)
admin.site.register(MpesaPayment)
admin.site.register(TruckingAssistance)
admin.site.register(ShippingInfo)
admin.site.register(WareHousing)
admin.site.register(HomeMoving)
