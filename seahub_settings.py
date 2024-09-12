[root@localhost conf]# cat seahub_settings.py 
# -*- coding: utf-8 -*-
SECRET_KEY = "b'd75(lu4ny63%gh97o4mc#tfbfx$$w%@*a53xi2@ush=(-ydrot'"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seahub-db',
        'USER': 'seafile',
        'PASSWORD': 'Tuyou#2024',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

