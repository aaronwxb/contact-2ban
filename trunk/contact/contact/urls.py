from django.conf.urls import patterns, include, url
from contact import views

urlpatterns = patterns('',
    (r'^login/$', views.login),
    (r'^$',  views.personalpage),
    (r'^personalpage/$', views.personalpage),
    (r'^modifyinfo/$', views.modifyinfo),
    (r'^modifyinfo/success/$', views.modifysuccess),
    (r'^checklogin/', views.check_login),
    (r'^accounts/login/$', views.login),
    (r'^classall/$', views.classall),
)
