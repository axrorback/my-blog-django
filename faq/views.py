from django.shortcuts import render

# Create your views here.
# faq/views.py
from django.shortcuts import render, redirect
from .models import FAQ
from .forms import FAQForm

def faq_list(request):
    faqs = FAQ.objects.filter(is_published=True).order_by('-created_at')

    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save() # yangi savol qo‘shiladi
            return redirect('faq_list')  # qayta yuklaymiz
    else:
        form = FAQForm()

    return render(request, 'faq/faq_list.html', {
        'faqs': faqs,
        'form': form
    })
