from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from . import views


urlpatterns = ['views.UploadPage',

    url(r'^', views.UploadPage, name='upload_page'),
    url(r'^', views.SaveFile, name='saved_page')
    ]
