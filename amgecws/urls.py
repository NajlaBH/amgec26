"""
URL configuration for lanseriws project.
Created by NajlaBH 11 OCT 25

"""

from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('imgs/favicon.ico'))),
     #Include admin apps urls
    path('admin/clearcache/', include('clearcache.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    #Include skelton app urls
    path('', include("skelton.urls")),
    #Include submissions app urls
    path('', include("submissions.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
