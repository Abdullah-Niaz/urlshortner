from django.contrib import admin
from .models import URL


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ("slug", "original_url", "created_at", "clicks")
    readonly_fields = ("created_at", "clicks")
    search_fields = ("slug", "original_url")
