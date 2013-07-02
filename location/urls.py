from django.conf.urls import patterns, url, include

urlpatterns = patterns('location.views',
    url(r'^$', 'index', name='location_home'),
    url(r'^details/(?P<identifier>\d+)$', 'details', name='location_details'),
    url(r'^details$', 'details', name='location_details_all'),
)
