from src.base.urls import Nurl
from django.urls import include
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    Nurl('') > 'src.news.views.Homepage',
    Nurl('news/') > 'src.news.views.NewsList',
    Nurl('news/<slug:slug>/') > 'src.news.views.NewsDetail',
    Nurl('about/') > 'src.news.views.AboutPage',
    Nurl('news/') > 'src.news.views.NewsList',
    Nurl('sport/') > 'src.news.views.SportList',
    Nurl('special/') > 'src.news.views.SpecialNews',
    Nurl('greetings/') > 'src.news.views.Greetings',
    Nurl('contact/') > 'src.news.views.Contact',
    Nurl('timeline/') > 'src.news.views.TimeLine',

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

