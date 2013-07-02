from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
# from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings
admin.autodiscover()

from page.models import PageCategory

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newhorizons.views.home', name='home'),
    # url(r'^newhorizons/', include('newhorizons.foo.urls')),
    # url(r'^robots.txt', direct_to_template, {'template' : 'robots.txt'}),
    # url(r'^robots.txt', TemplateView.as_view(template_name = 'robots.txt')),
    url(r'^$', 'newhorizons.views.home', name='home'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    url(r'^contact_us$', 'newhorizons.views.contactus', name='contactus'),
    url(r'^register$', 'newhorizons.views.register', name='register'),
    url(r'^register_target$', 'newhorizons.views.register_target', name='register_target'),
    url(r'^register_course$', 'newhorizons.views.register_course', name='register_course'),
    url(r'^register_class$', 'newhorizons.views.register_class', name='register_class'),
    
    url(r'^advert/',       include('advert.urls')),
    url(r'^blogs/',        include('blog.urls')),
    url(r'^courses/',      include('course.urls')),
    url(r'^instructors/',  include('instructor.urls')),
    url(r'^inthenews/',    include('inthenews.urls')),
    url(r'^locations/',    include('location.urls')),
    url(r'^news/',         include('news.urls')),
    url(r'^page/',         include('page.urls')),
    url(r'^testimonials/', include('testimonial.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Enable localization support
    url(r'^i18n/', include('django.conf.urls.i18n')),
    
    # Enable TinyMCE
    url(r'^tinymce/', include('tinymce.urls')),
)

urlpatterns += staticfiles_urlpatterns()
