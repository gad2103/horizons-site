from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^(?P<year>\d+)/(?P<trimester>\w+)$', 'list', name='blog_list_year_tri'),
    url(r'^$', 'list', name='blog_list'),
    url(r'^(?P<identifier>\d+)$', 'details', name='blog_details'),
    url(r'navigation/(?P<year>\d+)$', 'navigation', name='blog_navigation_year'),
    url(r'navigation', 'navigation', name='blog_navigation'),
    url(r'^authors/list$', 'author_list', name='blog_author_list'),
)
