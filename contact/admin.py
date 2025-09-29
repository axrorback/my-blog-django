from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_at")
    search_fields = ("title", "body")
    ordering = ("-updated_at",)
