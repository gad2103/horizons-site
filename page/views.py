from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from banner.models import BannerCategory
from blog.models import Blog, LocalizedBlog
from course.models import Class
from course.views import current_class_list, upcoming_class_list
from newhorizons.views import news_list, blog_list, getBanners
from news.models import News, LocalizedNews
from node.models import DataState, Language
from node.views import Paginate, LocalSet
from siteimage.models import SiteImage, SiteImageCategory
from page.models import Page, PageCategory, LocalizedPage
from sitemessage.views import get_message
from django.http import HttpResponse
    
def home_content(request, type, title="Index"):
    # Get the client language from the session
    language = Language.get_language(request)

    
    if language.pk != Language.DEFAULT:  # If a non-default language is requested, retrieve pages in that language.
        try:
            item = LocalizedPage.objects.get(meta__category=type, meta__title=title, language=language, data_state=DataState.PUBLISHED)
        except:
            try:
                item = LocalizedPage.objects.get(meta__category=type, meta__title=title, language=Language.DEFAULT, data_state=DataState.PUBLISHED)
            except:
                item = Page.objects.get(category=type, title=title, data_state=DataState.PUBLISHED)
    else:
        try:
            item = LocalizedPage.objects.get(meta__category=type, meta__title=title, language=Language.DEFAULT, data_state=DataState.PUBLISHED)
        except:
            item = Page.objects.get(category=type, title=title, data_state=DataState.PUBLISHED)
    
    #return (HttpResponse(str(type)))
    return render_to_response(
        'page/index.html',
        {'item': item,},
        context_instance=RequestContext(request))
    
def navigation(request, type, extra_links=None):
    #return HttpResponse(str('nagavation'))
    meta_queryset = Page.objects.filter(category = type, data_state=DataState.PUBLISHED).exclude(title = 'Index')
    queryset = LocalizedPage.objects.filter(meta__category = type, data_state=DataState.PUBLISHED).exclude(title = 'Index')
    new_queryset = LocalSet(request, meta_queryset, queryset)
    
    if type == PageCategory.ABOUTUS:
        template = 'page/navigation_aboutus.html'
    else:
        template = 'page/navigation.html'
    
    return render_to_response(
        template,
        {
            'page_list': new_queryset,
        },
        context_instance=RequestContext(request))
    
def list(request, type):
    
    #return HttpResponse(str('list'))
    meta_queryset = Page.objects.filter(category = type, data_state=DataState.PUBLISHED)
    queryset = LocalizedPage.objects.filter(meta__category = type, data_state=DataState.PUBLISHED)
    new_queryset = LocalSet(request, meta_queryset, queryset)
    
    # Set pagination
    list = Paginate(request, new_queryset,1)
    
    return render_to_response(
        'page/list.html',
        {
         'list': list,
        },
        context_instance=RequestContext(request))
  
def details(request, identifier):
    #return HttpResponse(str('details'))
    # Get the client language from the session
    language = Language.get_language(request)
    item = getItem(request, Page, LocalizedPage, identifier)
            
    page_no = request.GET.get('page_no')
    
    return render_to_response(
        'page/index.html',
        {
         'item': item,
         'page_no': page_no,
        },
        context_instance=RequestContext(request))

def contact(request, identifier=''):
    
    banners = getBanners(request, BannerCategory.ABOUT)
    try:
        left_nav_image = SiteImage.objects.get(category=SiteImageCategory.ABOUT)
    except Exception:
        left_nav_image = None
        
    if identifier:
        main_url = reverse('page_details', kwargs={'identifier': identifier})    
        title = getItem(request, Page, LocalizedPage, identifier).title
            
    header = mark_safe(title)
    
    return render_to_response(
        'page/contact.html',
        {'banners': banners,
         'main_url': main_url,
         'header': header,
         'left_nav_image': left_nav_image,
         },
        context_instance=RequestContext(request))

def aboutus(request, identifier=''):
    banners = getBanners(request, BannerCategory.ABOUT)
    try:
        left_nav_image = SiteImage.objects.get(category=SiteImageCategory.ABOUT)
    except Exception:
        left_nav_image = None
    
    if identifier == '':
        main_url = reverse('aboutus_home')
        header = _('about us')
    elif identifier == 'testimonials':
        main_url = reverse('testimonials')
        header = mark_safe('<a href="' + reverse('aboutus') + '">' + _('about us') + '</a><div class="divider"></div>' + _('testimonials'))
    elif identifier == 'inthenews':
        main_url = reverse('inthenews_list')
        header = mark_safe('<a href="' + reverse('aboutus') + '">' + _('about us') + '</a><div class="divider"></div>' + _('new horizons in the news'))
    else:
        main_url = reverse('page_details', kwargs={'identifier': identifier})
        title = getItem(request, Page, LocalizedPage, identifier).title
        header = mark_safe('<a href="' + reverse('aboutus') + '">' + _('about us') + '</a><div class="divider"></div>' + title)
    
    return render_to_response(
        'page/aboutus.html',
        {'banners': banners,
         'main_url': main_url,
         'header': header,
         'left_nav_image': left_nav_image,
         'none_message': get_message('about us'),
         },
        context_instance=RequestContext(request))
    
def newsandevents(request, identifier=None):
    
    if identifier:
        content_url = reverse('news_details', kwargs={'identifier':getItem(request, News, LocalizedNews, identifier).pk})
    else:
        content_url = reverse('news_list')
    
    banners = getBanners(request, BannerCategory.NEWS_EVENTS)
    try:
        left_nav_image = SiteImage.objects.get(category=SiteImageCategory.NEWS_EVENTS)
    except Exception:
        left_nav_image = None
    
    return render_to_response(
        'page/news_and_events.html',
        {
            'banners': banners,
            'left_nav_image': left_nav_image,
            'identifier': identifier,
            'content_url': content_url,
        },
        context_instance=RequestContext(request))
    
def blog(request, identifier=None):
    if identifier:
        content_url = reverse('blog_details', kwargs={'identifier':getItem(request, Blog, LocalizedBlog, identifier).pk})
    else:
        content_url = reverse('blog_list')
    
    recent_news = news_list(request, 10)
    return HttpResponse(content_url)
    
    banners = getBanners(request, BannerCategory.BLOG)
    try:
        left_nav_image = SiteImage.objects.get(category=SiteImageCategory.BLOG)
    except Exception:
        left_nav_image = None
    
    return render_to_response(
        'page/blog.html',
        {'banners': banners,
         'left_nav_image': left_nav_image,
         'news_list': recent_news,
         'content_url': content_url,
         },
        context_instance=RequestContext(request))
    
def getItem(request, model, localizedmodel, identifier):
    #return HttpResponse(str('getItem called'))
    language = Language.get_language(request)
    # Get the localized item in the requested language, otherwise return the default language, otherwise return the meta data.
    
    try:
        meta_item = model.objects.get(pk=identifier, data_state=DataState.PUBLISHED)
        try:
            item = localizedmodel.objects.get(meta__pk=identifier, language=language, data_state=DataState.PUBLISHED)
        except:
            if language.pk != Language.DEFAULT:
                try:
                    item = localizedmodel.objects.get(meta__pk=identifier, language=Language.DEFAULT, data_state=DataState.PUBLISHED)
                except:
                    item = meta_item
            else:
                item = meta_item
    except:
        try:
            item = localizedmodel.objects.get(pk=identifier, language=language, data_state=DataState.PUBLISHED)
        except:
            if language.pk != Language.DEFAULT:
                try:
                    item = localizedmodel.objects.get(pk=identifier, language=Language.DEFAULT, data_state=DataState.PUBLISHED)
                except:
                    item = None
            else:
                item = None
                
    return item
