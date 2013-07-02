from django.conf.urls import patterns, url

from advert.models import AdvertCategory

urlpatterns = patterns('advert.views',
    url(r'^$', 'item', name='advert'),
    url(r'^la$', 'item', {'type' : AdvertCategory.LA_COURSE}, name='advert_la'),
    url(r'^tp$', 'item', {'type' : AdvertCategory.TP_COURSE}, name='advert_tp'),
)
