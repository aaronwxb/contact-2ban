from django.conf.urls import patterns, include, url
from contact import views

urlpatterns = patterns('',
    (r'^login/$', views.login),
    (r'^information/$', views.information),
    (r'^modifyinfo/$', views.modifyinfo),
    (r'^modifyinfo/success/$', views.modifysuccess),
)
