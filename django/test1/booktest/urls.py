from django.conf.urls import include, url
from booktest.views import *
# Create your views here.

urlpatterns = [
    url(r'^zouzhenxing/', zouzhenxing),
    url(r'^show/(\d+)', show),
]

