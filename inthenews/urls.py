from django.conf.urls import patterns, url

urlpatterns = patterns('inthenews.views',
    url(r'^$', 'list', name='inthenews_list'),
    )
