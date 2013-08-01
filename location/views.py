from django.shortcuts import render_to_response
from django.template import RequestContext

from banner.models import BannerCategory
from location.models import Location, LocalizedLocation
from newhorizons.views import news_list, blog_list, getBanners
from node.models import Language, DataState
from node.views import LocalSet
from siteimage.models import SiteImage, SiteImageCategory
    
def index(request):
    meta_queryset = Location.objects.all()
    queryset = LocalizedLocation.objects.filter(data_state=DataState.SUBMITTED)
    new_queryset = LocalSet(request,meta_queryset,queryset)
    banners = getBanners(request, BannerCategory.LOCATIONS)
    try:
        left_nav_image = SiteImage.objects.get(category=SiteImageCategory.LOCATIONS)
    except Exception:
        left_nav_image = None
    recent_news = news_list(request, 5)
    recent_blogs = blog_list(request, 5)
    
    print DataState.PUBLISHED 
    return render_to_response(
        'locations/index.html',
        {'object_list': new_queryset,
         'banners': banners,
         'left_nav_image': left_nav_image,
         'news_list': recent_news,
         'blog_list': recent_blogs,},
        context_instance=RequestContext(request))
    
    
def details(request, identifier=None):
    
    # Get the client language from the session
    language = Language.get_language(request)
    
    if language.pk != Language.DEFAULT:  # If a non-default language is requested, retrieve pages in that language.
        try:
            queryset = LocalizedLocation.objects.get(meta=identifier, language=language)
        except:
            try:
                queryset = LocalizedLocation.objects.get(meta=identifier, language=Language.DEFAULT)
            except:
                queryset = Location.objects.get(pk=identifier)
    else:
        try:
            queryset = LocalizedLocation.objects.get(meta=identifier, language=Language.DEFAULT)
        except:
            queryset = Location.objects.get(pk=identifier)
    return render_to_response(
        'locations/details.html',
        {'location': queryset,},
        context_instance=RequestContext(request))
    
