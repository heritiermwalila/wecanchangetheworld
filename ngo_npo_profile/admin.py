from django.contrib import admin
from .models import Organisation, Page


class OrganisationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'email', 'phone')


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', "belong_to")
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Page, PageAdmin)

