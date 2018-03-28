from django.conf.urls import url 
from . import views 
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^dashboard$', views.dashboard),
    url(r'^dashboard/add$', views.add),
    url(r'^(?P<name>[\w ]+)/show$', views.show),
    url(r'^(?P<name>[\w ]+)/favorite$', views.favorite)
]
