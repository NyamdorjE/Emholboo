from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Course(models.Model):
    title = models.CharField(verbose_name=_('Title'),max_length=150)
    description = models.TextField(verbose_name=_('Description'),max_length= 200, null=True)
    image = models.ImageField(verbose_name=_('Image Field'), upload_to='cat_images', default='cat_images/default.jpg')

    class Meta:
        verbose_name= "Course"
        verbose_name_plural = "Courses"
        ordering = ['title']

    def __str__(self):
        return '{}'.format(self.title)

class Subject(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    slug = models.SlugField(verbose_name=_('Slug'),)
    title = models.CharField(verbose_name=_('Title'), max_length=30)
    course = models.ForeignKey(Course,verbose_name=_('Class'),on_delete=models.CASCADE)
    description = models.TextField(verbose_name=_('Description'),max_length=400)
    krijuar_me = models.DateTimeField(auto_now=True)
    image_lendes = models.ImageField(verbose_name=_('Image Field'), upload_to='kurs_images', default='default.jpg')

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
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
    slug = models.SlugField(verbose_name=_('Slug'))
    title = models.CharField(verbose_name=_('Title'), max_length=30)
    lenda = models.ForeignKey(Subject, verbose_name=_('Subject'),on_delete=models.CASCADE)
    video_id = models.CharField(verbose_name=_('Video id'), max_length=11)
    position = models.IntegerField(verbose_name=_('Position'))

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"course_slug": self.lenda.slug,'lesson_slug':self.slug})
