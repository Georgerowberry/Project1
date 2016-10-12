from django.conf.urls import url
from . import views

urlpatterns = [
#/members.
    url(r'^$', views.index, name='index'),
#members/123
    url(r'^(?P<member_id>[0-9]+)/$', views.detail, name='member_details'), 


]
