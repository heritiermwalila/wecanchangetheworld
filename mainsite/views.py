from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from changemakers.models import ChangeMaker
from service_provider.models import ServiceProvider, Page as ServicePage
from .models import Event, Opportunity, Category, ContactForm, Post, Quote, VideoPost
from .forms import Subscriber
from ngo_npo_profile.models import Organisation, Page as NGONPOPages
from companies.models import Company, Page


def index(request):

    if request.method == 'POST':
        subscriberForm = Subscriber(request.POST)

        if subscriberForm.is_valid():
            instance = subscriberForm.save(commit=False)
            instance.save()
            messages.success(request, 'Thanks for subscribing to our newsletter')

    else:
        subscriberForm = Subscriber()

    """

    :param request:
    :return:
    """
    headlines = Post.objects.filter(type_of_the_post='headline').order_by('-date_posted')[:3]
    company_news = Post.objects.filter(type_of_the_post='company-news').order_by('-date_posted')[:3]
    news = Post.objects.filter(type_of_the_post='news').order_by('-date_posted')[:3]
    lastest_news = Post.objects.filter(type_of_the_post='news').order_by('-date_posted')[:4]
    quotes = Quote.objects.all().order_by('-date_posted')[:2]
    changeMakers = ChangeMaker.objects.filter(status='published')
    opportunities = Opportunity.objects.all().order_by('-date_posted')[:3]
    events = Event.objects.all().order_by('-start_date')[:3]
    videoposts = VideoPost.objects.all().order_by('-date_posted')[:3]
    ngo_npo = Organisation.objects.all().order_by('-date_posted')[:6]


    """
    """
    return render(request, 'pages/index.html', {
        "title": 'Welcome',
        'headlines': headlines,
        'companynews': company_news,
        'news': news,
        'headsides': lastest_news,
        'quotes': quotes,
        'changeMakers': changeMakers,
        'opportunities': opportunities,
        'events': events,
        'videoposts': videoposts,
        'ngo_npo': ngo_npo,
        'subscriberform': subscriberForm,
        'active': True})


def post(request):

    posts_list = Post.objects.filter(status='published').order_by('-date_posted')
    paginator = Paginator(posts_list, 3)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'pages/post.html', {'title': 'News', 'posts': posts})


def single_post(request, slug):

    post = get_object_or_404(Post, slug=slug)
    return render(request, 'pages/single_post.html', {'title': post.title, 'post': post})


def change_makers(request):

    changemakers = ChangeMaker.objects.filter(status='published').order_by('-date_created')

    return render(request, 'pages/change_makers.html', {'changemakers': changemakers, 'title':'Change Makers', 'active': True})


def change_maker_single(request, slug):

    changemaker = get_object_or_404(ChangeMaker, slug=slug)
    return render(request, 'pages/change_maker_single.html', {'changemaker':changemaker, 'active': True})


def directory(request):
    return render(request, 'pages/directory.html', {'title': 'Directory', 'active': True})


def events(request):

    events = Event.objects.all()
    return render(request, 'pages/events.html', {'events':events, 'title':'Events', 'active': True})

def event_single(request, slug):

    event = get_object_or_404(Event, slug=slug)
    return render(request, 'pages/event_single.html', {'event': event, 'active': True})

def about_us(request):
    return render(request, 'pages/about_us.html', {'title': 'About us', 'active': True})


def contact_us(request):

    if request.method == 'GET':
        form = ContactForm()

    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject=subject, message=message, from_email=email, recipient_list=['webdivinecreativity@gmail.com', ])
            except BadHeaderError:
                return HttpResponse('Invalid header response')

            return redirect('success')

    return render(request, 'pages/contact_us.html', {'title': 'Contact Us', 'form': form})


def successView(request):

    return render(request, 'pages/success.html')


def subscribe(request):

    if request.method == 'POST':
        form = Subscriber(request.POST)

        if form.is_valid():
            messages.success(request, "Thanks for subscribing to our newsletters. You'll be notify of the following:")
            subscriber = form.save(commit=False)
            subscriber.save()
            form = Subscriber()
    else:
        form = Subscriber()

    return render(request, 'pages/subscribe.html', {'title': 'subscriber', 'form': form})


def opportunities(request):
    opportunities = Opportunity.objects.all()
    return render(request, 'pages/opportunities.html', {'title': 'Opportunities', 'opportunities': opportunities, 'active': True})


def profile(request, username):

    changemaker = get_object_or_404(ChangeMaker, id=username).order_by('-date_created')
    return render(request, 'pages/change_makers_profile.html', {'changemaker': changemaker, 'active': True})


def category(request, slug):

    category_name = get_object_or_404(Category, slug=slug)
    posts_list = Post.objects.filter(category__slug=slug).order_by('-date_posted')
    return render(request, 'pages/post_by_category_page.html', {'category': category_name, 'posts': posts_list, 'active': True})


def ngo_npo(request):

    ngo_npo = Organisation.objects.all()

    return render(request, 'pages/ngo_npo.html', {'title': 'NGO & NPO', 'ngonpos': ngo_npo, 'active': True})


def ngo_npo_profile(request, slug):

    organisation = get_object_or_404(Organisation, slug=slug)
    pages = NGONPOPages.objects.filter(organisation_id=organisation.id)
    posts = Post.objects.filter(ngo_or_npo_id=organisation.id)
    title = organisation.name

    return render(request, 'pages/ngo_npo_profile.html', {
        'title': title,
        'pages': pages,
        'posts': posts,
        'organisation': organisation
        })

def companies(request):

    companies = Company.objects.all().order_by('-name')

    return render(request, 'pages/companies.html', {'title': 'Companies', 'companies': companies})


def company_profile(request, slug):

    company = get_object_or_404(Company, slug=slug)
    pages = Page.objects.filter(company=company.id)
    posts = Post.objects.filter(company_id=company.id)
    return render(request, 'pages/company_profile.html', {
        'title': company.name,
        'company': company,
        'pages': pages,
        'posts': posts

    })


def service_provider(request):

    services = ServiceProvider.objects.all().order_by('-name')

    return render(request, 'pages/ngo_npo_service_provider.html', {
        'title': 'NGO & NPO Service Provider',
        'services': services
    })


def service_provider_profile(request, slug):

    service_provider = get_object_or_404(ServiceProvider, slug=slug)
    pages = ServicePage.objects.filter(service_provider_id=service_provider.id)
    posts = Post.objects.filter(service_provider_id=service_provider.id)
    return render(request, 'pages/service_provider_profile.html', {
                            'title': service_provider.name,
                            'pages': pages,
                            'posts': posts,
                            'service_provider': service_provider
                            })
