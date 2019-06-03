from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.shortcuts import reverse

class Company(models.Model):
    name = models.CharField(max_length=100, help_text=u'Organisation name')
    email = models.EmailField(help_text=u'Company Email', blank=True)
    phone = models.CharField(max_length=50 , blank=True)
    ceo = models.CharField(max_length=50, blank=True)
    logo = models.FileField(verbose_name='Profile logo',
                            upload_to='media/static/images/%Y/%m/%d',
                            default='static/images/noprofile.png')
    expect = models.TextField(max_length=255, help_text=u'Expect text', blank=True)
    slug = models.SlugField(unique=True)
    website = models.URLField(name='website_url', help_text=u'website Address', blank=True)
    background_image = models.FileField(upload_to='static/images/%Y', default='static/images/defaultbg.jpg')


    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company-profile', kwargs={'slug': self.slug})


class Page(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    content = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.name

    def belong_to(self):
        return self.company.name
