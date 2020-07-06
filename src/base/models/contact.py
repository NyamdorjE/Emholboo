from django import forms
from django.shortcuts import render

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(default='')
    Phone = models.CharField(max_length=10, default='')
    message = models.TextField()

    class Meta:
        verbose_name = "Холбоо барих"
        ordering = ['name']

    def __str__(self):
        return self.name


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "Phone", 'email', 'message']
        labels = {'name': "Нэр",
                  "Phone": "Утас",
                  'email': 'Имайл',
                  'message': 'Хүсэлт',
                  }

        from django.shortcuts import render


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


admin.site.register(Contact)
