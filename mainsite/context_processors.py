from .models import Category, Event


def categories(request):

    categories_list = Category.objects.all().order_by('name')

    return {
        'categories': categories_list,
    }


def events(request):

    events_list = Event.objects.all().order_by('-start_date')

    return {
        'events': events_list
    }