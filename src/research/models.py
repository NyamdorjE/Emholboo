from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class ResearchCategory(models.Model):
    title = models.CharField(max_length= 255 , verbose_name=_('Research Category '))
    
    class Meta:
        verbose_name = "Судалгааны Бүлэг"
        verbose_name_plural= "Судалгааны бүлэгүүд"
        ordering = ['title']
        
    def __str__(self):
        return self.title
    
class Research(models.Model):
    category = models.ForeignKey(ResearchCategory, verbose_name=_("Category"), on_delete=models.CASCADE, related_name="Research")
    title = models.CharField(max_length=255, verbose_name=_('Гарчиг'), )
    slug = models.SlugField(max_length=255, verbose_name=_('Slug'), unique=True)
    author = models.CharField(max_length=255, verbose_name=_('Үүсгэсэн'))
    content = RichTextField(blank=True, null=True, verbose_name=_('Контэнт'))
    image = models.ImageField(verbose_name=('Зураг'), upload_to='media/research/')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_('Хэзээ үүсгэсэн'))
    updated_on = models.DateTimeField(auto_now= True,  verbose_name=_('Хэзээ засварласан'))
    
    class Meta:
        verbose_name = "Судалгаа"
        verbose_name_plural = "Судалгаанууд"
        ordering = ['created_on']
        
    def __str__(self):
        return self.title


class LawCategory(models.Model):
    title = models.CharField(max_length= 255 , verbose_name=_('Хууль тогтоомж '))
    
    class Meta:
        verbose_name = "Хууль бүлэг"
        verbose_name_plural= "Хууль тогтоомж бүлэг"
        ordering = ['title']
        
    def __str__(self):
        return self.title
    

class Law(models.Model):
    category = models.ForeignKey(LawCategory, verbose_name=_('Хууль бүлэг'), on_delete=models.CASCADE, related_name='Law', blank=True, default="1")
    title = models.CharField(verbose_name=_('Гарчиг'), max_length=128)
    pdf_file = models.FileField(verbose_name=_('Файл хийх'), upload_to='pdf_file', null=True, blank=True)
    views = models.IntegerField(default=0, editable=False)
    created_at = models.DateTimeField(verbose_name=_('Хэзээ үүсгэсэн'), auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name=_('Хэзээ засварласан'), auto_now=True)
    
    class Meta:
        verbose_name = _('Хууль тогтоомж')
        verbose_name_plural = _('Хууль тогтоомж')
        ordering = ['title']

    def __str__(self):
        return u'{0}'.format(self.title)
