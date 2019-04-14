from django.conf.urls import url
from booktest.views import *

urlpatterns = [
    url(r'^(\d+)$', index, name='index'),
    url(r'^(\d+)/(\d+)/$', show),
    url(r'^(?P<p2>\d+)/(?P<p1>\d+)/(?P<p3>\d+)/$', mygod),

    url(r'^getTest1/$', getTest1),
    url(r'^getTest2/$', getTest2),
    url(r'^getTest3/$', getTest3),

    url(r'^postTest1$', postTest1),
    url(r'^postTest2$', postTest2),

    url(r'^$', index1),
    url(r'^cookies/$', cookies_test),

    url(r'^index2$', index2),
    url(r'^index3$', index3),

    url(r'^json$', json),
]
