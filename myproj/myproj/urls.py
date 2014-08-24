from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'myapp.views.salam'),
    url(r'^resty/', 'myapp.views.salamresty'),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns2 = staticfiles_urlpatterns()
urlpatterns = urlpatterns2 + urlpatterns