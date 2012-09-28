from django.conf.urls import patterns, include, url
from contact import views

urlpatterns = patterns('',
    (r'^login/$', views.login),
    (r'^personalpage/$', views.personalpage),
    (r'^modifyinfo/$', views.modifyinfo),
    (r'^modifyinfo/success/$', views.modifysuccess),
)
