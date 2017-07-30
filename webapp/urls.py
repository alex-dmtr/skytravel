from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^_events/$', views.PartialEvents.as_view(), name='api_events'),
    url(r'^cities/(?P<slug>[\w-]+)/$', views.CityDetail.as_view(), name='city'),
]