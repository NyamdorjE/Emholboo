from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _


class CourseCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))

    class Meta:
            verbose_name = "Сургалтын Бүлэг"
            verbose_name_plural = "Сургалтын бүлэгүүд"
            ordering = ['title']

    def __str__(self):
        return self.title
   
           

class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete = models.CASCADE, related_name="Course_category", null=True)
    title = models.CharField(max_length=150, verbose_name=_('Гарчиг'))
    description = models.TextField(max_length= 200, null=True, verbose_name=_('Тайлбар'))
    image = models.ImageField(upload_to='cat_images', default='cat_images/default.jpg', verbose_name=_('Зураг'))
    students = models.ManyToManyField(User, swappable=True, verbose_name=_('Сурагчид'))
    class Meta:
            verbose_name = "Курс"
            verbose_name_plural = "Курс"
            ordering = ['title']

    def __str__(self):
        return '{}'.format(self.title)

class Subject(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE, verbose_name=_('Үүсгэсэн '))
    title = models.CharField(max_length=30, verbose_name=_('Гарчиг'))
    slug = models.SlugField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE, verbose_name=_('Курс'))
    description = models.TextField(max_length=400, verbose_name=_('Тайлбар'))
    created_on = models.DateTimeField(auto_now=True, verbose_name=_('Хэзээ үүсгэсэн'))
    image_field = models.ImageField(upload_to='kurs_images', default='default.jpg', verbose_name=_('Зураг оруулах'))
    class Meta:
            verbose_name = "Сэдэв"
            verbose_name_plural = "Сэдэв"
            ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

    def get_courses_related_to_memberships(self):
        return self.courses.all()

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')




class Lesson(models.Model):
    title = models.CharField(max_length=30, verbose_name=_(' Хичээлийн гарчиг'))
    slug = models.SlugField()
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE, verbose_name=_('Сэдэв'))
    video_id = models.FileField(upload_to="course_video", blank=True, null=True , verbose_name=_('Бичлэг хийх'))
    content = RichTextField(verbose_name=_('Контент'))
    position = models.IntegerField(verbose_name=_('Хичээлийн байрлал'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"course_slug": self.subject.slug,'lesson_slug':self.slug})
    
    class Meta:
            verbose_name = "Хичээл"
            verbose_name_plural = "Хичээл"
            ordering = ['title']


class Post(models.Model):
    post = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
