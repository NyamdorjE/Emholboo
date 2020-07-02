from django.db import models

# Create your models here.


class Courses(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=255)
    description = models.TextField(verbose_name=_("description"), max_length=500, null=True)
    image = models.ImageField(upload_to='cat_images', default='cat_images/default.jpg')


class Subjects(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    slug = models.SlugField()
    title = models.CharField(verbose_name=_('Title'), max_length=30)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    description = models.TextField(verbose_name=_('Description'), max_length=400)
    created_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='Subject_images', default='default.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

    def get_courses_related_to_users(self):
        return self.courses.all()

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')
    
class Lessons(models.Model):
    slug = models.SlugField()
    title = models.CharField(verbose_name=_('Title')max_length=30)
    subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=11)
    position = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"course_slug": self.subjects.slug,'lesson_slug':self.slug})
    


