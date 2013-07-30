import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.http import HttpResponse

from blog.models import Blog, LocalizedBlog,Author, LocalizedAuthor
from course.models import Target, TargetCategory
from node.models import DataState, Language
from node.views import Paginate, LocalSet
from sitemessage.views import get_message
from news.views import date_helper

def list(request, year=None, trimester=None):
    
    '''if not year or not trimester:
        this_date = datetime.datetime.today()
        year = this_date.year
        this_trimester = (this_date.month-1)/3
        trimester = '1' # Oct-Nov-Dec
    
    if trimester == '4':
        to_year = int(year)+1
    else:
        to_year = int(year)
        
    from_time = datetime.datetime.strptime(str(int(trimester)*3-2) + ' 1 '+ str(year), '%m %d %Y')
    to_time = datetime.datetime.strptime(str((int(trimester)*3+1)%12) + ' 1 '+ str(to_year), '%m %d %Y')
    print to_time
      '''  
    from_time, to_time = date_helper(trimester,year)
    meta_queryset = Blog.objects.filter(published__gt=from_time, published__lt=to_time, data_state=DataState.PUBLISHED).order_by('-published')
    queryset = LocalizedBlog.objects.filter(published__gt=from_time, published__lt=to_time, data_state=DataState.PUBLISHED).order_by('-published')
    new_queryset = LocalSet(request, meta_queryset, queryset)
    
    for item in new_queryset:
        item.details_url = reverse('blog_details', kwargs={'identifier': item.pk})
    
    none_message = get_message('no blog')
    
    # Set pagination
    list = Paginate(request, new_queryset, 5)
    
    return render_to_response(
        'list2.html',
        {
         'type': 'blog',
         'list': list,
         'url': reverse('blog_list'),
         'year': year,
         'trimester': trimester,
         'none_message': none_message,
        },
        context_instance=RequestContext(request))
    
def details(request, identifier):
    # Get the client language from the session
    language = Language.get_language(request)
    
    # Get the localized item in the requested language, otherwise return the default language, otherwise return the meta data.
    if language.pk != Language.DEFAULT:  # If a non-default language is requested, retrieve pages in that language.
        try:
            item = LocalizedBlog.objects.get(pk=identifier, language=language, data_state=DataState.PUBLISHED)
        except:
            try:
                item = LocalizedBlog.objects.get(pk=identifier, language=Language.DEFAULT, data_state=DataState.PUBLISHED)
            except:
                item = Blog.objects.get(pk=identifier, data_state=DataState.PUBLISHED)
    else:
        try:
            item = LocalizedBlog.objects.get(pk=identifier, language=Language.DEFAULT, data_state=DataState.PUBLISHED)
        except:
            item = Blog.objects.get(pk=identifier, data_state=DataState.PUBLISHED)
            
    page_no = request.GET.get('page_no') # Needed to know which page in the paginator to return to
    year = request.GET.get('year')
    trimester = request.GET.get('trimester')
    
    return render_to_response(
        'details.html',
        {
         'item': item,
         'page_no': page_no,
         'year': year,
         'trimester': trimester,
         'url': reverse('blog_list'),
        },
        context_instance=RequestContext(request))

def navigation(request, year=None):
    
    # Get the client language from the session
    language = Language.get_language(request)
    this_date = datetime.datetime.today()
    year_list = range(this_date.year, 2012, -1)
    if year == None:
        year = year_list[0]
    if int(year) == this_date.year:
        trimester_list = [('1', _('Jan-Feb-Mar'))]
        if this_date.month > 3:
            trimester_list.insert(0,('2', _('Apr-May-Jun')))
        if this_date.month > 6:
            trimester_list.insert(0,('3', _('Jul-Aug-Sep')))
        if this_date.month > 9:
            trimester_list.insert(0,('4', _('Oct-Nov-Dec')))
    else:
        trimester_list = [
                ('4', _('Oct-Nov-Dec')),
                ('3', _('Jul-Aug-Sep')),
                ('2', _('Apr-May-Jun')),
                ('1', _('Jan-Feb-Mar'))
        ]
    
    
    return render_to_response(
        'trimester_nav.html',
        {
         'type': 'blog',
         'year_list': year_list,
         'expand': year,
         'trimester_list': trimester_list,
         },
        context_instance=RequestContext(request))
def author_list(request):
    meta_queryset = Author.objects.filter(data_state=DataState.PUBLISHED)
    queryset = LocalizedAuthor.objects.filter(data_state=DataState.PUBLISHED)
    new_queryset = LocalSet(request, meta_queryset, queryset)
    
    list = Paginate(request, new_queryset, 3)
    '''if type == TargetCategory.TESTPREPARATIONS:
        url = reverse('tp_instructor_list')
    elif type == TargetCategory.LANGUAGEARTS:
        url = reverse('la_instructor_list')
   ''' 
    url="dummy"
    return render_to_response(
        'authors/details.html',
        {
            'details_list': list,
            'url': url,
        },
        context_instance=RequestContext(request)
    )
