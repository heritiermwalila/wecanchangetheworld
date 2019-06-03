from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class ServiceProvider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    ceo = models.CharField(max_length=50, blank=True)
    logo = models.FileField(upload_to='static/images/service-provider/', default='static/images/noprofile.png')
    expect = models.TextField(max_length=368, help_text='Short description for the profile')
    description = RichTextUploadingField(help_text=u'Profile description. use col in your HMTL tag to create column')
    slug = models.SlugField()
    website = models.URLField(name='website_url', help_text=u'website Address', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    background_image = models.FileField(upload_to='static/images/%Y', default='static/images/defaultbg.jpg')

    def __str__(self):
        return self.name



class Page(models.Model):
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    content = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.name

    def belong_to(self):
        return self.service_provider.name



