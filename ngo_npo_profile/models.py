from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.shortcuts import reverse


class Organisation(models.Model):
    name = models.CharField(max_length=100, help_text=u'Organisation name')
    slug = models.SlugField(unique=True)
    email = models.EmailField(help_text=u'Organisation Email', blank=True)
    phone = models.CharField(max_length=50, blank=True)
    ceo = models.CharField(max_length=50, blank=True)
    logo = models.FileField(verbose_name='Profile logo',
                            upload_to='ngo-npo/',
                            default='static/images/noprofile.png')
    expect = models.TextField(max_length=255, help_text=u'Expect text', blank=True)
    website = models.URLField(name='website_url', help_text=u'website Address', blank=True)
    background_image = models.FileField(upload_to='ngo-npo/', default='static/images/defaultbg.jpg')
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Organisation'
        verbose_name_plural = 'Organisations'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ngo-npo-single', kwargs={'slug': self.slug})


class Page(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    content = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.name

    def belong_to(self):
        return self.organisation.name
