from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_at")
    search_fields = ("title", "content")
    ordering = ("-updated_at",)
