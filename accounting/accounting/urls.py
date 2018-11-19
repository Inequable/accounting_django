"""accounting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path,include
from . import view, utils
from django.conf import settings
from django.conf.urls import url
# from accounting.utils import verifycode

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', view.hello),
    path('index/', include('index.url')), # 将index app的url.py路由文件导入进主app中，进行调用
    # path('captcha/', include('captcha.urls')),
    url(r'^verifycode/$', utils.verifycode, name='image'), # python 验证码 name 是用来反向解析路径的
]

if settings.DEBUG is False:
    urlpatterns += patterns('', url(r'^public/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}), )
