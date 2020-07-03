from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=256)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']

    def __str__(self):
        return u'{0}'.format(self.name)

