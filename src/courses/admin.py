from django.contrib import admin
from src.courses.models import Subject,Lesson,Course,CourseCategory
# Register your models here.


admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CourseCategory)


