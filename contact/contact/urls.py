from django.conf.urls import patterns, include, url
from contact import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^hello/$', views.hello),
    (r'^time/$', views.current_datetime),
    (r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    (r'^login/$', views.login),
    (r'^information/$', views.information),
)
