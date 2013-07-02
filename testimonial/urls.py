from django.conf.urls import patterns, url

from testimonial.models import TestimonialCategory

urlpatterns = patterns('testimonial.views',
    url(r'^$', 'list', name='testimonials'),
    url(r'^sample$',       'sample', name='testimonial_sample'),
    url(r'^languagearts$', 'list', {'type': TestimonialCategory.LANGUAGEARTS}, name='la_testimonials'),
    url(r'^testprep$',     'list', {'type': TestimonialCategory.TESTPREPARATIONS}, name='tp_testimonials'),
    )
