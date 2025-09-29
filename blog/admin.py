from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_published")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}  # slug avtomatik title’dan olinadi
    ordering = ("-created_at",)
