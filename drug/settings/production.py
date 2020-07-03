# -*- coding:utf-8 -*-

"""
Production settings
"""

from .common import *

DEBUG = True
ALLOWED_HOSTS = ['10.0.0.153', 'localhost']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'emholboo',
        'USER': 'emholboo',
        'PASSWORD': '#DiyjoT42u#M',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
