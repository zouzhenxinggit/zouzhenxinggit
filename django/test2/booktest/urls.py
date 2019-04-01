from django.conf.urls import include, url
from django.contrib import admin
from booktest.views import *


urlpatterns = [
    url(r'^$', index)
]
