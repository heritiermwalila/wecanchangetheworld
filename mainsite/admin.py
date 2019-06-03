
from django.contrib import admin
from .models import Event, Opportunity, Category, Post, CategoryToPost, Quote, VideoPost, Subscriber, Newsletter


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'start_date', 'end_date', 'organisation_name', 'end_time')


class OpportunityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'date_posted', 'company_name', 'location', 'city')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'description')


class CategoryToPostInline(admin.TabularInline):
    model = CategoryToPost
    extra = 1


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('author',)
    inlines = [CategoryToPostInline]
    search_fields = ['title']
    list_display = ('title', 'date_posted')
    list_filter = ['date_posted']

    class Meta:
        model = Post

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author',)


class VideoPostAdmin(admin.ModelAdmin):
    list_display = ("title", "date_posted")
    prepopulated_fields = {"slug": ("title",)}


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_posted')


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('title', 'status')
    search_fields = ['title']

admin.site.register(Event, EventAdmin)
admin.site.register(Opportunity, OpportunityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(VideoPost, VideoPostAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
