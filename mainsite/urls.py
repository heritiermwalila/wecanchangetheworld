from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('post/', views.post, name="post"),
    path('post/<slug>', views.single_post, name='post-single'),
    path('change-makers/', views.change_makers, name="change-makers"),
    path('change-makers/<slug>', views.change_maker_single),
    path('directory/', views.directory, name="directory"),
    path('events/', views.events, name="events"),
    path('events/<slug>', views.event_single),
    path('about-us/', views.about_us, name="about-us"),
    path('contact-us/', views.contact_us, name="contact-us"),
    path('subscribe/', views.subscribe, name="subscribe"),
    path('opportunities/', views.opportunities, name="opportunities"),
    path('change-makers/profile/<username>', views.profile),
    path('category/<slug>', views.category),
    path('ngo-npo/', views.ngo_npo, name="ngo-npo"),
    path('ngo-npo/<slug>', views.ngo_npo_profile, name='ngo-npo-single'),
    path('companies/', views.companies, name="companies"),
    path('companies/<slug>', views.company_profile, name='company-profile'),
    path('ngo-npo-service-provider/', views.service_provider, name="service-provider"),
    path('ngo-npo-service-provider/<slug>', views.service_provider_profile),
    path('success/', views.successView, name='success')
]