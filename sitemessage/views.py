import sys
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from sitemessage.models import SiteMessage, LocalizedSiteMessage
from node.views import Language, LocalItem

def get_message(name, language=None, request=None):
    
    if not language:
        language = Language.get_language(request)
    
    try:
        meta_item = SiteMessage.objects.get(name=name)
        try:
            item = LocalizedSiteMessage.objects.get(meta=meta_item, language=language)
        except Exception:
            item = LocalizedSiteMessage.objects.get(meta=meta_item, language=Language.DEFAULT)
        return item.text
    except Exception:
        sys.exc_clear()
        return ''
    
