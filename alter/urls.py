from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^start$', views.start, name='start'),
    url(r'^send$', views.send, name='send'),
    url(r'^$', views.hello, name='hello'),
]