from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.core.mail import send_mail
from django.shortcuts import reverse
from datetime import date
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from service_provider.models import ServiceProvider
from django import forms
from django.contrib.auth.models import User
from ngo_npo_profile.models import Organisation
from companies.models import Company


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = RichTextUploadingField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    postType = (
        ('headline', 'headline'),
        ('company-news', 'company-news'),
        ('news', 'news'),
    )
    status = (
        ('draft', 'draft'),
        ('published', 'published'),
    )
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text=u'Site author')
    category = models.ManyToManyField(Category, blank=True, through='CategoryToPost')
    post_owner = models.CharField(max_length=50, blank=True,
                                  help_text=u'Insert an author in case the author did not own that')
    slug = models.SlugField(max_length=150, unique=True)
    image_url = models.FileField(upload_to='post/', default='static/images/postnoimage.png')
    expect = models.TextField(max_length=255)
    content = RichTextUploadingField()
    date_posted = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=255, blank=True)
    is_breaking_news = models.BooleanField(default=False, blank=True)
    type_of_the_post = models.CharField(max_length=50, choices=postType, blank=True)
    status = models.CharField(choices=status, default='draft', max_length=10)
    ngo_or_npo = models.ForeignKey(Organisation,
                                        blank=True,
                                        help_text=u'please assign post to NGO or NPO',
                                        on_delete=models.CASCADE,
                                        null=True
                                        )
    company = models.ForeignKey(Company,
                                     blank=True,
                                     help_text=u'Assign post to Company',
                                     on_delete=models.CASCADE,
                                     null=True
                                    )
    service_provider = models.ForeignKey(ServiceProvider,
                                blank=True,
                                help_text=u'Assign post to Service Provider',
                                on_delete=models.CASCADE,
                                null=True
                                )
    # show_on_banner = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-single', kwargs={'slug': self.slug})


class CategoryToPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Event(models.Model):
    name = models.CharField(max_length=100, help_text=u'Event name')
    slug = models.SlugField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text=u'Category name')
    start_date = models.DateField(u'Starting Date', default=date.today, help_text=u'Starting Date')
    end_date = models.DateField(u'Ending Date', help_text=u'Ending Date')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Ending time', help_text=u'Ending time')
    organisation_name = models.CharField(max_length=100, blank=True)
    organisation_email = models.EmailField()
    organisation_phone = models.CharField(max_length=15, blank=True)
    event_main_guest = models.FileField(upload_to='events/', default='static/images/noprofile.png')
    event_main_guest_name = models.CharField(max_length=100, blank=True)
    event_address = models.CharField(max_length=255, blank=True)
    venue_name = models.CharField(max_length=50, blank=True)
    expect = models.TextField(max_length=368)
    notes = RichTextUploadingField(blank=True)
    ngo_or_npo = models.ForeignKey(Organisation,
                                        on_delete=models.CASCADE,
                                        blank=True,
                                        null=True,
                                        help_text=u'Assign Event to NGO, NPO or leave blank',
                                        )
    company = models.ForeignKey(Company,
                                     blank=True,
                                     null=True,
                                     on_delete=models.CASCADE,
                                     help_text=u'Assign Event to Company or leave blank',
                                     )
    service_provider = models.ForeignKey(ServiceProvider,
                                         blank=True,
                                         help_text=u'Assign post to Service Provider',
                                         on_delete=models.CASCADE,
                                         null=True
                                         )

    class Meta:
        verbose_name = u'Event'
        verbose_name_plural = u'Events'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event-single', kwargs={'slug': self.slug})





class Opportunity(models.Model):
    locations = (
        ('Eastern Cape', 'Eastern Cape'),
        ('Free State', 'Free State'),
        ('Gauteng', 'Gauteng'),
        ('KwaZulu-Natal', 'KwaZulu-Natal'),
        ('Limpopo', 'Limpopo'),
        ('Mpumalanga', 'Mpumalanga'),
        ('North West', 'North West'),
        ('Northern Cape', 'Northern Cape'),
        ('Western Cape', 'Western Cape'),
    )
    terms = (
        ('Fixed Term', 'Fixed Term'),
        ('Permanent', 'Permanent'),
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=2)
    date_posted = models.DateTimeField(default=timezone.now)
    expect = models.TextField(max_length=150, blank=True)
    description = RichTextUploadingField()
    company_name = models.CharField(max_length=100, blank=True)
    company_email = models.EmailField(blank=True)
    role = models.CharField(max_length=50, blank=True)
    reporting_to = models.CharField(max_length=50, blank=True)
    employment_term = models.CharField(max_length=20, choices=terms, blank=True)
    location = models.CharField(max_length=20, choices=locations)
    city = models.CharField(max_length=50, blank=True)
    company_logo = models.FileField(upload_to='opportunities/',
                                    default='/static/images/wecanchangeopportunity.jpg')
    ngo_or_npo = models.ForeignKey(Organisation,
                                        blank=True,
                                        on_delete=models.CASCADE,
                                        null=True,
                                        help_text=u'Assign Opportunity to NGO, NPO or leave blank',
                                        )
    company = models.ForeignKey(Company,
                                     blank=True,
                                     on_delete=models.CASCADE,
                                     null=True,
                                     help_text=u'Assign Opportunity to Company or leave blank',
                                     )
    service_provider = models.ForeignKey(ServiceProvider,
                                         blank=True,
                                         help_text=u'Assign post to Service Provider',
                                         on_delete=models.CASCADE,
                                         null=True
                                         )

    class Meta:
        verbose_name = u'Jobs'
        verbose_name_plural = u'Jobs'

    def __str__(self):
        return self.name


class Quote(models.Model):
    author = models.CharField(max_length=100)
    quote_note = models.TextField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)


class ContactForm(forms.Form):
    firstname = forms.CharField(label='First Name', max_length=50)
    lastname = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(label='Email Address', max_length=100)
    phone = forms.CharField(label='Cellphone', max_length=20)
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)


class VideoPost(models.Model):
    title = models.CharField(max_length=100, help_text=u'Video title', blank=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    url = models.URLField(name='video_url', blank=True, help_text=u'example: http://www.youtube/myvideourl')
    ngo_or_npo = models.ForeignKey(Organisation,
                                   blank=True,
                                   help_text=u'please assign post to NGO or NPO',
                                   on_delete=models.CASCADE,
                                   null=True
                                   )
    company = models.ForeignKey(Company,
                                blank=True,
                                help_text=u'Assign post to Company',
                                on_delete=models.CASCADE,
                                null=True
                                )
    service_provider = models.ForeignKey(ServiceProvider,
                                         blank=True,
                                         help_text=u'Assign post to Service Provider',
                                         on_delete=models.CASCADE,
                                         null=True
                                         )
    date_posted = models.DateTimeField(default=timezone.now)


class Banner(models.Model):
    status = (
        ('active', 'Active'),
        ('deactivate', 'Deactivate'),
    )
    banner_file = models.FileField(upload_to='banners/', blank=True),
    ngo_npo = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    activate = models.CharField(choices=status, default='deactivate', max_length=20)


class Subscriber(models.Model):
    email = models.EmailField(unique=True, )
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email




@receiver(post_save, sender=Subscriber)
def send_confirm_message(sender, instance, **kwargs):

    message = """
    
        Thank you for subscribing to our newsletter.
        
        Please note you will start receiving our news everytime we publish one.
        
        regards
        we can change our world
    
    """

    send_mail('Subscription to newsletter', message, 'webdivinecreativity@gmail.com', [instance.email])


class Newsletter(models.Model):
    choices = (
        ('draft', 'Draft'),
        ('send', 'Send')
    )
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    status = models.CharField(choices=choices, max_length=10)
    date_to_be_sent = models.DateTimeField(default=timezone.now)
    organisation = models.ForeignKey(Organisation,
                                     on_delete=models.CASCADE,
                                     help_text=u'Select to assign this newsletter', null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, help_text=u'Select to assign this newsletter', null=True, blank=True)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE,
                                         help_text=u'Select to assign this newsletter',  null=True, blank=True)


@receiver(post_save, sender=Newsletter)
def changeStatus(sender, instance, **kwargs):
    if instance.status == 'send':
        # send email to all subscribers
        subscribers_list = []
        body = instance.content
        news_subject = instance.title
        subscribers = Subscriber.objects.all()
        for s in subscribers:
            subscribers_list.append(s.email)
    return send_mail(news_subject, body, 'weddivinecreativity@gmail.com', subscribers_list)