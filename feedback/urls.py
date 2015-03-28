from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^add/', views.add_feedback, name='add_feedback')
)
