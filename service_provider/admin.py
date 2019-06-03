from django.contrib import admin
from .models import ServiceProvider, Page


class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ("name", )
    prepopulated_fields = {"slug": ("name",)}


class PageAdmin(admin.ModelAdmin):
    list_display = ("name", "belong_to")
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(ServiceProvider, ServiceProviderAdmin)
admin.site.register(Page, PageAdmin)