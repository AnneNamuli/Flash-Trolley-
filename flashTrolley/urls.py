from django.conf.urls import patterns, include, url
from flashTrolley.views import home, register, user_login,logout_page, view_product
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^register/$',register, name='register'),
                       url(r'^$', view_product, name='signin'),
                       url(r'^home/$', home),
                       url(r'^signin/$', user_login),
                       url('', include('social.apps.django_app.urls', namespace='social')),
                       url('', include('django.contrib.auth.urls', namespace='auth')),
                       url(r'^$', 'django.contrib.auth.views.login'),
                       url(r'^logout/$',logout_page),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
                       )
