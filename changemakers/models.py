from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class ChangeMaker(models.Model):

    TITLE = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    status = (
        ('draft', 'draft'),
        ('published', 'published'),
    )
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, unique=True)
    image_url = models.FileField(default='static/images/noprofile.png')
    organisation = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=4, choices=TITLE)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    expect = models.TextField(help_text=u'Insert expect text', blank=True)
    description = RichTextField()
    status = models.CharField(choices=status, max_length=50)
    date_created = models.DateTimeField(default=timezone.now)





