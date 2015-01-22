from django.conf.urls import patterns, include, url
from django.contrib import admin
from wiki import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^new/', views.createPage.as_view(), name='page-new',),
    
	)
