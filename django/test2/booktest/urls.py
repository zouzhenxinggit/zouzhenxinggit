from django.conf.urls import include, url
from django.contrib import admin
from booktest.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index)
]
