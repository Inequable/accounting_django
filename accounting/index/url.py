# -*- coding: utf-8 -*-

from django.urls import path
from index.views import *

urlpatterns = [
	path('login/', login),
	path('index/', main),
	path('account/', account),
	path('bill/', bill),
	path('sortManagement/', sortManagement),
    path('logout/', logout),
]