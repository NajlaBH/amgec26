# Urls of submissions app
# BY NAJLA BH OCT 25

from django.urls import path, include

from . import views
urlpatterns=[
  path("abstractsubmission",views.abstractsubmit, name='abstractsubmission'),
]