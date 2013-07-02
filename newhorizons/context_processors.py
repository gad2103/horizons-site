from django.conf import settings

from node.models import DataState, Language
from node.views import LocalSet
from page.models import Page, LocalizedPage, PageCategory

def site_settings(context):
    return {
        'DEBUG': settings.DEBUG,
        'PROJECT_ROOT': settings.PROJECT_ROOT,
        'STATIC_ROOT': settings.STATIC_ROOT,
        'STATIC_URL': settings.STATIC_URL
        }

def site_menu(request):
    language = Language.get_language(request)
    
    meta_queryset1 = Page.objects.filter(category=PageCategory.CONTACT, data_state=DataState.PUBLISHED).exclude(title = 'Index')
    queryset1 = LocalizedPage.objects.filter(meta__category=PageCategory.CONTACT, data_state=DataState.PUBLISHED).exclude(title = 'Index')
    contact_queryset = LocalSet(request, meta_queryset1, queryset1)
    
    meta_queryset2 = Page.objects.filter(category=PageCategory.ABOUTUS, data_state=DataState.PUBLISHED).exclude(title = 'Index')
    queryset2 = LocalizedPage.objects.filter(meta__category=PageCategory.ABOUTUS, data_state=DataState.PUBLISHED).exclude(title = 'Index')
    about_queryset = LocalSet(request, meta_queryset2, queryset2)
    
    menu={}
    menu[0] = contact_queryset
    menu[1] = about_queryset
    
    return {'menu': menu,}

