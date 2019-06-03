from django.utils.text import slugify


def unique_slug_generator(model, field_name):

    slug = slugify(field_name)
    unique_slug = slug
    num = 1
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    return unique_slug


