# Urls of skelton app
# BY NAJLA BH OCT 25

from django.urls import path, include

from . import views
urlpatterns=[
  path("",views.home, name='index'),
  path("index",views.home, name='index'),
  path("about",views.about, name='about'),
  path("topics",views.topics, name='topics'),
  path("sponsors",views.sponsors, name='sponsors'),
  path("contact",views.contact, name='contact'),
  path("fees",views.fees, name='fees'),
  path("committees",views.committees, name='committees'),
  path("workshop",views.workshop, name='workshop'),
  path("program",views.program, name='program'),
  path("private",views.private, name='private'),
]