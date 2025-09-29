from django.db import models

# Create your models here.
from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=150, help_text="Contact sahifasi uchun sarlavha")
    body = models.TextField(help_text="Contact sahifasi matni (masalan, email, telegram, manzil va boshqalar)")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
