from .models import Category, Post


def categories(request):

    categories_list = Category.objects.all().order_by('name')
    posts = Post.objects.all()

    return {
        'categories': categories_list,
    }