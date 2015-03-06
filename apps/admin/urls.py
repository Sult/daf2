from django.conf.urls import patterns, url

from apps.admin import views

urlpatterns = patterns('',
    url(r'^admin/$', views.admin, name="admin"),
    url(r'^admin/users/$', views.admin_users, name="admin_users"),
    url(r'^admin/user/(?P<pk>\d+)/confirm/$', views.user_confirm, name='user_confirm'),
    url(r'^admin/user/(?P<pk>\d+)/delete/$', views.user_delete, name='user_delete'),
    
    #news admin
    url(r'^admin/news/$', views.news_admin, name='news_admin'),
    url(r'^admin/news/create/$', views.news_create, name='news_create'),
    url(r'^admin/news/edit/(?P<slug>[\w-]+)/$', views.news_edit, name='news_edit'),
    
    #blog admin
    url(r'^admin/blog/$', views.blog_admin, name='blog_admin'),
    url(r'^admin/blog/create/$', views.blog_create, name='blog_create'),
    url(r'^admin/blog/preview/(?P<slug>[\w-]+)/$', views.blog_preview, name='blog_preview'),
    url(r'^admin/blog/edit/(?P<slug>[\w-]+)/$', views.blog_edit, name='blog_edit'),
    url(r'^admin/blog/delete/(?P<pk>\d+)/$', views.blog_delete, name='blog_delete'),
)

