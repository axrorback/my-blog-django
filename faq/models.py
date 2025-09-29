# faq/models.py
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class FAQ(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z\s]+$',
                message="Faqatgina harflar va bo'sh joy kiritilishi kerak"
            )
        ]
    )
    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{9,15}$',
                message="Telefon raqam to‘g‘ri formatda bo‘lishi kerak. Masalan: +998901234567"
            )
        ]
    )
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    # yangi maydonlar
    answered_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    answered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.question[:30]}"

    def masked_phone(self):
        return self.phone[:4] + "****" + self.phone[-2:]
