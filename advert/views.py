import sys
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render

from node.models import DataState

from advert.models import Advert, AdvertCategory

def item(request, type=AdvertCategory.GENERAL):
    
    item = None
    try:
        item = Advert.objects.get(category = type, data_state=DataState.PUBLISHED)
    except Exception:
        try:
            item = Advert.objects.get(data_state=DataState.PUBLISHED)
        except Exception:
            sys.exc_clear()
    
    return render(
        request,
        'advert.html',
        {
            'item': item,
        },
        context_instance=RequestContext(request))