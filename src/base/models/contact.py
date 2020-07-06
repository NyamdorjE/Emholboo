from django.db import models
from django.forms import ModelForm
from django.shortcuts import render
from django.db import models
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory


class contact(models.Model):

    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class contact(ModelForm):
    class Meta:
        model = contact
        fields = ['title', 'notes']


# Create your views here.


def contact(request):

    if request.method == 'POST':
        form = contact(request.POST)
        if form.is_valid():

            u = form.save()
            users = contact.objects.all()

            return render(request, 'contact.html', {'users': users})

    else:
        form_class = contact

    return render(request, 'contact.html', {
        'form': form_class,
    })
