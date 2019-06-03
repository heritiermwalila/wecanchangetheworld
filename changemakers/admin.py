from django.contrib import admin
from .models import ChangeMaker


class ChangeMakerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'title', 'email', 'phone')


admin.site.register(ChangeMaker, ChangeMakerAdmin)

