import sys
from models import Settings, LocalizedSettings
from node.views import LocalItem


def settings(request):
    try:
        site_settings = Settings.objects.get(name='Analytics, Favicon, Header, Footer')
    except Exception:
        dict = {}
        sys.exc_clear()
        return dict
    
    item = LocalItem(site_settings, LocalizedSettings, request=request)
    dict = {'favicon': item.meta.favicon,
            'copyrights': item.copyrights,
            'moto': item.moto,
            'analytics': item.meta.analytics,
            'contactus': item.contact_footer,
            }
    
    return dict
