from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = ['City', 'District', 'Khoroo']


class City(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=128)

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        ordering = ['name']

    def __str__(self):
        return u'{0}'.format(self.name)


class District(models.Model):
    city = models.ForeignKey(
        City,
        verbose_name=_('City'),
        on_delete=models.CASCADE
    )
    name = models.CharField(verbose_name=_('Name'), max_length=128)

    class Meta:
        verbose_name = _('District')
        verbose_name_plural = _('Districts')
        ordering = ['name']

    def __str__(self):
        return u'{0}'.format(self.name)


class Khoroo(models.Model):
    district = models.ForeignKey(
        District,
        verbose_name=_('District'),
        on_delete=models.CASCADE
    )
    name = models.CharField(verbose_name=_('Name'), max_length=128)

    class Meta:
        verbose_name = _('Khoroo')
        verbose_name_plural = _('Khoroos')
        ordering = ['name']

    def __str__(self):
        return u'{0}'.format(self.name)
