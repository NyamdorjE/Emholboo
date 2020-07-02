from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
# Register your models here.

class PharmacistConfig(AppConfig):
    name = 'src.pharmacist'
    verbose_name = _('Pharmacist')