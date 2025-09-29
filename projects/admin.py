from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_active")
    list_filter = ("is_active", "created_at")
    search_fields = ("title", "description")
    ordering = ("-created_at",)
