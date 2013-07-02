from django.conf.urls import patterns, url

from page.models import PageCategory

urlpatterns = patterns('page.views',
    
    url(r'^newsandevents$', 'newsandevents', name='newsandevents'),
    url(r'^newsandevents/(?P<identifier>\d+)$', 'newsandevents', name='newsandevents_page'),
    url(r'^blog$', 'blog', name='blog'),
    url(r'^blog/(?P<identifier>\d+)$', 'blog', name='blog_page'),
    url(r'^aboutus$', 'aboutus', name='aboutus'),
    url(r'^aboutus/navigation$', 'navigation',       {'type': PageCategory.ABOUTUS}, name='aboutus_navigation'),
    url(r'^aboutus/home$', 'home_content',        {'type': PageCategory.ABOUTUS}, name='aboutus_home'),
    url(r'^aboutus/page/(?P<identifier>\w+)$', 'aboutus', name='aboutus_page'),
    url(r'^contact/(?P<identifier>\w+)$', 'contact', name='contact_page'),
    url(r'^details/(?P<identifier>\w+)$', 'details', name='page_details'),
    
    url(r'^tp_homepage$', 'home_content',         {'type': PageCategory.TESTPREPARATIONS}, name='tp_home_page'),
    url(r'^la_homepage$', 'home_content',         {'type': PageCategory.LANGUAGEARTS}, name='la_home_page'),
    url(r'^cc_homepage$', 'home_content',         {'type': PageCategory.CURRICULUMCONSULTING}, name='cc_home_page'),
    url(r'^ac_homepage$', 'home_content',         {'type': PageCategory.ADMISSIONSCONSULTING}, name='ac_home_page'),
    url(r'^tp_instructor_homepage$', 'home_content', {'type': PageCategory.TP_INSTRUCTORS}, name='tp_instructor_home_page'),
    url(r'^la_instructor_homepage$', 'home_content', {'type': PageCategory.LA_INSTRUCTORS}, name='la_instructor_home_page'),
    url(r'^tp_schedule_homepage$', 'home_content', {'type': PageCategory.TP_SCHEDULES}, name='tp_schedule_home_page'),
    url(r'^la_schedule_homepage$', 'home_content', {'type': PageCategory.LA_SCHEDULES}, name='la_schedule_home_page'),
    
    url(r'^news_homepage$', 'list',       {'type': PageCategory.NEWSandEVENTS}, name='news_home_page'),
    url(r'^location_homepage$', 'home_content',   {'type': PageCategory.LOCATIONS}, name='location_home_page'),
)
