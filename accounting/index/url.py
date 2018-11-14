# -*- coding: utf-8 -*-

from django.urls import path
from index.views import *

urlpatterns = [
	path('index', main),
]