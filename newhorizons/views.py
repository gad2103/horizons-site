import sys
from django import forms
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from banner.models import Banner, LocalizedBanner, BannerCategory
from blog.models import Blog, LocalizedBlog
from course.models import TargetCategory, LocalizedTargetCategory, Target, Course, Class
#from newhorizons.models import ContactForm, RegisterForm
from newhorizons.forms import ContactForm, RegisterForm, RegisterForm_target, RegisterForm_course, RegisterForm_class
from news.models import News, LocalizedNews
from node.models import DataState, Language
from node.views import LocalItem, LocalSet
from page.models import Page, PageCategory, LocalizedPage
from sitemessage.models import SiteMessage, LocalizedSiteMessage

def home(request):
    banners = getBanners(request, BannerCategory.HOME)
    
    meta_queryset = TargetCategory.objects.all()
    queryset = LocalizedTargetCategory.objects.all()
    new_queryset = LocalSet(request, meta_queryset, queryset)
    
    for item in new_queryset:
        if hasattr(item, 'meta'):
            id = item.meta.pk
        else:
            id = item.pk
            
        if id == 1:
            item.style = 'tp'
            item.link = reverse('testpreparations_home')
        elif id == 2:
            item.style = 'la'
            item.link = reverse('languagearts_home')
        elif id == 7:
            item.style = 'ac'
            item.link = reverse('admissionscounseling_home')
        elif id == 3:
            item.style = 'cc'
            item.link = reverse('curriculumconsulting_home')
    recent_news = news_list(request,1)
    recent_blogs = blog_list(request,1)
    
    return render_to_response(
        'home.html',
        {'banners': banners,
         'portals': new_queryset,
         'blog_list': recent_blogs,
         'news_list': recent_news,
         },
        context_instance=RequestContext(request))
    
def news_list(request, number):
    meta_queryset = News.objects.filter(data_state=DataState.PUBLISHED).order_by('-published')
    queryset = LocalizedNews.objects.filter(data_state=DataState.PUBLISHED).order_by('-published')
    new_queryset = LocalSet(request, meta_queryset, queryset)
    
    return new_queryset[:number]
    
def blog_list(request, number):
    meta_queryset = Blog.objects.filter(data_state=DataState.PUBLISHED).order_by('-published')
    queryset = LocalizedBlog.objects.filter(data_state=DataState.PUBLISHED).order_by('-published')
    new_queryset = LocalSet(request, meta_queryset, queryset)
                
    return new_queryset[:number]

def contactus(request):
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        if form.is_valid():
            message = {}
            for key, value in form.cleaned_data.items():
                message[key] = value
            subject = message['subject']
            from_email = message['sender']
            to_email = 'info@horizonsprep.com'
            template_html = loader.get_template("emails/contact.html")
            template_txt = loader.get_template("emails/contact.txt")
            ct = Context({ 'n': message, })
            msg_html = template_html.render(ct)
            msg_txt = template_txt.render(ct)
            msg = EmailMultiAlternatives(subject, msg_txt, from_email, [to_email])
            msg.attach_alternative(msg_html, "text/html")
            msg.send()
            return HttpResponseRedirect('/')
        else:
            pass
    else:
        form = ContactForm()
        
    try:
        info1 = SiteMessage.objects.get(name='contact form note')
        message = LocalItem(info1, LocalizedSiteMessage, request=request)
    except Exception:
        message = None
        sys.exc_clear()
        
    try:
        info2 = SiteMessage.objects.get(name='contact form address')
        address = LocalItem(info2, LocalizedSiteMessage, request=request)
    except Exception:
        address = None
        sys.exc_clear()
        
    banners = getBanners(request, BannerCategory.CONTACT)
        
    return render(
        request,
        'forms/contactus.html',
        {
            'banners': banners,
            'form': form,
            'message': message,
            'address': address,
        })

def register(request):
    if request.method == 'POST':
        #import pdb; pdb.set_trace()
        form = RegisterForm(request.POST)
        if form.is_valid():
            message = {}
            for key, value in form.cleaned_data.items():
                message[key] = value
            subject = 'Registration for ' + message['student_name']
            from_email = message['parent_email']
            to_email = 'info@horizonsprep.com'
            template_html = loader.get_template("emails/registration.html")
            template_txt = loader.get_template("emails/registration.txt")
            ct = Context({ 'n': message, })
            msg_html = template_html.render(ct)
            msg_txt = template_txt.render(ct)
            msg = EmailMultiAlternatives(subject, msg_txt, from_email, [to_email])
            msg.attach_alternative(msg_html, "text/html")
            msg.send()
            return HttpResponseRedirect('/')
        else:
            pass
    else:
        a_course = request.GET.get('course')
        if a_course:
            form = RegisterForm()
            course_instance = Course.objects.get(pk=a_course)
            
            # Filter the allowed values of the dropdowns.
            form.fields['classes'].queryset = Class.objects.filter(course=a_course)
            form.fields['courses'].queryset = Course.objects.filter(target=course_instance.target)
            form.fields['targets'].queryset = Target.objects.filter(category=course_instance.target.category)
            
            # Set the default values of the dropdowns.
            form.initial['courses'] = a_course
            form.initial['targets'] = course_instance.target.pk
            form.initial['portals'] = course_instance.target.category.pk
            
        else:
            form = RegisterForm()
    
    try:
        info1 = SiteMessage.objects.get(name='registration form note')
        note = LocalItem(info1, LocalizedSiteMessage, request=request)
    except Exception:
        note = None
        sys.exc_clear()
        
    try:
        info2 = SiteMessage.objects.get(name='registration form message')
        message = LocalItem(info2, LocalizedSiteMessage, request=request)
    except Exception:
        message = None
        sys.exc_clear()
        
    banners = getBanners(request, BannerCategory.REGISTRATION)
            
    return render(
        request,
        'forms/register.html',
        {
            'banners': banners,
            'form': form,
            'message': message,
            'note': note
        })
    
def register_target(request):
    
    a_portal = request.GET.get('portal')
    form = RegisterForm_target()
    if a_portal =='0':
        form.fields['targets'].queryset = Target.objects.all()
    else:
        form.fields['targets'].queryset = Target.objects.filter(category=a_portal)
    
    return render(
        request,
        'forms/target_select.html',
        {
            'form': form
        })
    
def register_course(request):
    
    a_portal = request.GET.get('portal')
    a_target = request.GET.get('target')
    form = RegisterForm_course()
    if a_portal:
        if a_portal == '0':
            form.fields['courses'].queryset = Course.objects.all()
        else:
            form.fields['courses'].queryset = Course.objects.filter(target__category=a_portal)
    elif a_target:
        if a_target == '0':
            form.fields['courses'].queryset = Course.objects.all()
        else:
            form.fields['courses'].queryset = Course.objects.filter(target=a_target)
    
    return render(
        request,
        'forms/course_select.html',
        {
            'form': form
        })
    
def register_class(request):
    a_portal = request.GET.get('portal')
    a_target = request.GET.get('target')
    a_course = request.GET.get('course')
    form = RegisterForm_class()
    if a_portal:
        form.fields['classes'].queryset = Class.objects.filter(course__target__category=a_portal)
    elif a_target:
        form.fields['classes'].queryset = Class.objects.filter(course__target=a_target)
    elif a_course:
        form.fields['classes'].queryset = Class.objects.filter(course=a_course)
    
    return render(
        request,
        'forms/class_select.html',
        {
            'form': form
        })
    
def getBanners(request, category):
    meta_banners = Banner.objects.filter(category=category, data_state=DataState.PUBLISHED)
    banners = LocalizedBanner.objects.filter(meta__category=category, data_state=DataState.PUBLISHED)
    new_banners = LocalSet(request, meta_banners, banners)
    
    return new_banners
