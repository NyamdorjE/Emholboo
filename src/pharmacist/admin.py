from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Pharmacist
# Register your models here.

class PharmacistAdmin(admin.ModelAdmin):
    list_display = ['email']



admin.site.register(Pharmacist, PharmacistAdmin)
