from django.conf.urls import patterns, include, url
from views import HomePageView
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lisitra.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^$' , HomePageView.as_view(), name='home'),
)

