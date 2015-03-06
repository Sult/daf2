from django.conf.urls import patterns, url

from apps.blog import views

urlpatterns = patterns('',
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<slug>[\w-]+)/$', views.blog_article, name='blog_article'),
)

