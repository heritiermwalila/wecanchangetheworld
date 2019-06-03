from django.contrib import admin
from .models import Company, Page


class PageToCompanyInline(admin.TabularInline):
    model = Page


class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    # inlines = [PageToCompanyInline]


class PageAdmin(admin.ModelAdmin):
    list_display = ("name", "belong_to")
    prepopulated_fields = {"slug": ("name",)}
    # search_fields = ['name', 'belong_to']


admin.site.register(Company, CompanyAdmin)
admin.site.register(Page, PageAdmin)