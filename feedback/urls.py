from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^add/', views.AddFeedbackView.as_view(), name='add_feedback')
)
