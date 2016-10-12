from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', (admin.site.urls)),
    url(r'^members/', include('members.urls')),
    url(r'^upload/', include('upload.urls')),
]
