from django.contrib import admin
from relationships.models import Passport, Citizen, Order, Customer

# Register your models here.
admin.site.register(Citizen)
admin.site.register(Passport)
admin.site.register(Customer)
admin.site.register(Order)

