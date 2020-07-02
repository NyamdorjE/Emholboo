from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User




class Pharmacist(models.Model):
    user = models.OneToOneField(User,verbose_name=_('User'), on_delete=models.CASCADE, editable=False )
    surname = models.CharField(verbose_name=_('Surname'), max_length=128)
    fristname = models.CharField(verbose_name=_('Frist name '), max_length=128)
    register = models.CharField(verbose_name=_('Register NO'), max_length=16)
    email= models.EmailField(verbose_name=_('Email'))
    phone = models.CharField(verbose_name=_('Phone'), max_length=16)
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated at'), auto_now=True)
    created_by = models.ForeignKey(User, verbose_name=_('Created by'), on_delete=models.CASCADE, related_name='created_user', editable=False)
    updated_by = models.ForeignKey(User, verbose_name=_('Updated by'), on_delete=models.CASCADE, related_name='update_user', editable=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)


    class Meta:
        verbose_name = _('Pharmacist')
        verbose_name_plural = _('Pharmacists')
        ordering = ['-updated_at']
        
    def __str__(self):
        return self.fristname    
    

