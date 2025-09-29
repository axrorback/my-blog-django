# faq/forms.py
from django import forms
from .models import FAQ

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['name', 'phone', 'question']  # user faqat bularni kiritadi
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingizni kiriting'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+998901234567'}),
            'question': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Savolingizni yozing...'}),
        }
