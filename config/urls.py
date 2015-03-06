from django.conf.urls import patterns, include, url
#from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^', include('apps.users.urls')),
    url(r'^', include('apps.apies.urls')),
    url(r'^', include('apps.characters.urls')),
    url(r'^', include('apps.static.urls')),
    url(r'^', include('apps.blog.urls')),
    url(r'^', include('apps.admin.urls')),
    
    url(r'^froala_editor/', include('froala_editor.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
