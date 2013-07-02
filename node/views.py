import sys
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def Paginate(request, queryset, item_per_page=10):
    page = request.GET.get('page')
    paginator = Paginator(queryset, item_per_page)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        list = paginator.page(paginator.num_pages)
    return list

from node.models import DataState, Language

def LocalItem(meta_objet, localized_model, state=None, request=None):
    found = False
    if request:
        language = Language.get_language(request)
        if state:
            try:
                localized_item = localized_model.objects.get(meta=meta_objet.pk, language=language, data_state=state)
                found = True
            except Exception:
                found = False
                sys.exc_clear()
        else:
            try:
                localized_item = localized_model.objects.get(meta=meta_objet.pk, language=language)
                found = True
            except Exception:
                found = False
                sys.exc_clear()
    if not found:    
        if state:
            for language in Language.PRIORITY:
                try:
                    localized_item = localized_model.objects.get(meta=meta_objet.pk, language=language, data_state=state)
                    found = True
                except Exception:
                    sys.exc_clear()
                if True:
                    break
        else:
            for language in Language.PRIORITY:
                try:
                    localized_item = localized_model.objects.get(meta=meta_objet.pk, language=language)
                    found = True
                except Exception:
                    sys.exc_clear()
                if True:
                    break
    if found:
        return localized_item
    else:
        return False

def LocalSet(request, meta_queryset, queryset):
    # Assumes Language.DEFAULT exists
    new_queryset = []
    
    # Get the client language from the session
    language = Language.get_language(request)
    
    # Get the localized item in the requested language, otherwise return the default language, otherwise return the meta data.
    if language.pk != Language.DEFAULT:  # If a non-default language is requested, retrieve pages in that language.
            
        local_queryset = []
        for item in queryset:
            if item.language == language:
                local_queryset.append(item)
                    
        fallback_queryset = []
        for item in queryset:
            if item.language.pk == Language.DEFAULT:
                fallback_queryset.append(item)
        
        for meta_item in meta_queryset:
            found = False
            
            for item in local_queryset:
                if item.meta == meta_item:
                    new_queryset.append(item)
                    found = True
                    break
                
            if not found:
                for item in fallback_queryset:
                    if item.meta == meta_item:
                        new_queryset.append(item)
                        found = True
                        break;
                    
            if not found:
                new_queryset.append(meta_item)
    else:
        # Otherwise retrieve pages in the default language.
        for meta_item in meta_queryset:
            found = False
            for alt_lang in Language.PRIORITY:
                
                local_queryset = []
                for item in queryset:
                    if item.language.pk == alt_lang:
                        local_queryset.append(item)
                
                for item in local_queryset:
                    if item.meta == meta_item:
                        new_queryset.append(item)
                        found = True
                        break
                if found:
                    break
            if not found:
                new_queryset.append(meta_item)
    
    return new_queryset