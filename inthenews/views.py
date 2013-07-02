from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

from inthenews.models import Inthenews
from node.models import DataState, Language
from node.views import Paginate, LocalSet

def list(request):
    
    queryset = Inthenews.objects.filter(data_state=DataState.PUBLISHED).order_by('published')
    list = Paginate(request, queryset, 5)
    url = reverse('inthenews_list')
    
    return render_to_response(
        'list2.html',
        {
         'type': 'inthenews',
         'list': list,
         'url': url,
        },
        context_instance=RequestContext(request))
    
def details(request, identifier):
    
    item = News.objects.get(pk=identifier, data_state=DataState.PUBLISHED)
            
    page_no = request.GET.get('page_no') # Needed to know which page in the paginator to return to
    year = request.GET.get('year')
    trimester = request.GET.get('trimester')
    
    return render_to_response(
        'details.html',
        {
         'item': item,
         'page_no': page_no,
         'url': reverse('news_list'),
        },
        context_instance=RequestContext(request))