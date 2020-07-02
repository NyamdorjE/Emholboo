import secrets
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from src.courses.models import Courses, Subjects, Lessons
from src.users.models import Users
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators improt login_required
from django.contrib import messages



# Create your views here.

class CoursesVIew(TemplateVIew):
    
