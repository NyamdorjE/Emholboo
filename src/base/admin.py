from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _

from src.base import models as m





@admin.register(m.Category)
class CategoryAdmin(admin.ModelAdmin):

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}









