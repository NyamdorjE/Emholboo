from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext_lazy as _
import re
from django.db.models import Q
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Гарчиг'))
    category_type = (
        ("news", "News"),
        ("sport", "Sport"),
        ("research", "Research")
    )
    cate_type = models.CharField(
        max_length=255, choices=category_type, default="news")

    class Meta:
        verbose_name = "Мэдээний бүлэг"
        verbose_name_plural = "Мэдээний бүлэгүүд"
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_products(self):
        return News.objects.filter(category=self)


class News(models.Model):
    category = models.ForeignKey(Category, verbose_name=_(
        'Category'), on_delete=models.CASCADE, related_name="News")
    title = models.CharField(
        max_length=255, verbose_name=_('Гарчиг'), unique=True)
    slug = models.SlugField(
        max_length=255, verbose_name=_('Слаг'), unique=True)
    author = models.CharField(max_length=255, verbose_name=_('Үүсгэсэн'))
    content = RichTextField(blank=True, null=True, verbose_name=_('Контент'))
    image = models.ImageField(verbose_name=('Зураг'), upload_to='media/news/')
    created_on = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Хэзээ үүссэн'))
    updated_on = models.DateTimeField(
        auto_now=True,  verbose_name=_('Хэзээ засварласан'))
    is_special = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Нийтлэл"
        verbose_name_plural = "Нийтлэлүүд"
        ordering = ['-created_on']

    def __str__(self):
        return self.title


def handler404(request, exception):
    context = {}
    response = render(request, "pages/errors/404.html", context=context)
    response.status_code = 404
    return response


def handler500(request):
    context = {}
    response = render(request, "pages/errors/500.html", context=context)
    response.status_code = 500
    return response
