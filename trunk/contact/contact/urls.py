from django.conf.urls import patterns, include, url
from contact import views
from os import path

urlpatterns = patterns('',
    (r'^login/$', views.login),
    (r'^$',  views.login),
    (r'^personalpage/$', views.personalpage),
    (r'^modifyinfo/$', views.modifyinfo),
    (r'^modifyinfo/success/$', views.modifysuccess),
    (r'^checklogin/', views.check_login),
    (r'^accounts/login/$', views.login),
    (r'^classall/$', views.classall),
    (r'^error/$', views.error),
    (r'^handle_modify/$', views.handle_modify),
    (r'^about/$', views.about),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': path.join(path.abspath(path.dirname(__file__)), 'static'),
         'show_indexes': False}, name="static"),
)
