from django.conf.urls import patterns, url

urlpatterns = patterns('news.views',
    url(r'^$', 'list', name='news_list'),
    url(r'^(?P<year>\d+)/(?P<trimester>\w+)$', 'list', name='news_list_year_tri'),
    url(r'^page/(?P<identifier>\d+)$', 'details', name='news_details'),
    url(r'^navigation/(?P<year>\d+)$', 'navigation', name='news_navigation_year'),
    url(r'^navigation', 'navigation', name='news_navigation'),
    url(r'^preview$', 'sample', name='news_preview'),
    #url(r'^page/(?P<identifier>\d+)$', 'list_page', name=''),
)
