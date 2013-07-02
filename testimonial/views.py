from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _

from testimonial.models import Testimonial, LocalizedTestimonial, TestimonialCategory
from node.models import DataState, Language
from node.views import Paginate, LocalSet

def list(request, type=None):
    if type:
        meta_queryset = Testimonial.objects.filter(category = type, data_state=DataState.PUBLISHED)
        queryset = LocalizedTestimonial.objects.filter(meta__category = type, data_state=DataState.PUBLISHED)
    else:
        meta_queryset = Testimonial.objects.filter(data_state=DataState.PUBLISHED)
        queryset = LocalizedTestimonial.objects.filter(data_state=DataState.PUBLISHED)
    new_queryset = LocalSet(request, meta_queryset, queryset)
    
    # Set pagination
    list = Paginate(request, new_queryset)
    
    return render_to_response(
        'testimonials/list.html',
        {
         'type': 'testimonial',
         'list': list,
        },
        context_instance=RequestContext(request))
    
def sample(request):
    
    item = LocalizedTestimonial.objects.filter(language=Language.get_language(request), data_state=DataState.PUBLISHED).order_by('?')[:1]
    
    return render_to_response(
        'testimonials/panel_list.html',
        {
         'title': _('testimonials'),
         'type': 'testimonial',
         'list': item,
        },
        context_instance=RequestContext(request))
    