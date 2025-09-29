# faq/admin.py
from django.contrib import admin
from .models import FAQ
from django.utils import timezone

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('name', 'question', 'is_published', 'created_at', 'answered_by', 'answered_at')
    search_fields = ('name', 'phone', 'question', 'answer')
    list_filter = ('is_published', 'created_at')

    def save_model(self, request, obj, form, change):
        if obj.answer and not obj.answered_by:
            obj.answered_by = request.user
            obj.answered_at = timezone.now()
        super().save_model(request, obj, form, change)
