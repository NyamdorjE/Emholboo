"""drug URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from src.base.views import handler404, handler500
from src.poll import views as poll_views
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from src.accounts import views as user_views
from src.courses import views as courses_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('src.accounts.urls')),
    path('', include('src.news.urls')),
    path('', include('src.research.urls')),
    path('', include('src.poll.urls')),
    path('', include('src.courses.urls')),
    path('404/', handler404),
    path('500/', handler500),
    path('poll/', poll_views.home, name='poll'),
    path('create/', poll_views.create, name='create'),
    path('vote/<poll_id>/', poll_views.vote, name='vote'),
    path('results/<poll_id>/', poll_views.results, name='results'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    # path('search', search, name='blog-search'),
    



    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


