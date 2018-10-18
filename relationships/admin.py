from django.contrib import admin
from relationships.models import Passport, Citizen

# Register your models here.
admin.site.register(Citizen)
admin.site.register(Passport)

