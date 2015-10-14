#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'babyshow.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #home为主页面
    #url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^$','app.views.index',name = 'index'),
    url(r'^register/$','app.views.register',name = 'register'),
    url(r'^login/$','app.views.user_login',name = 'login'),
    url(r'^logout/$','app.views.user_logout',name = 'logout'),
    url(r'^vote/$','app.views.vote',name='vote'),
    url(r'^details/$','app.views.details',name = 'details'),
    url(r'^search/$','app.views.search',name = 'search'),
)
