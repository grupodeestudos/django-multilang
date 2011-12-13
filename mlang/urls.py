from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^blog/', include('blog.urls')),
    url(r'^(?P<lang>[a-zA-z_]+)/blog/', include('blog.urls')),
    url(r'^$', 'mlang.views.home'),
    url(r'^(?P<lang>[a-zA-Z_]+)$', 'mlang.views.home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
