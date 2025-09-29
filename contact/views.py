from django.shortcuts import render

# Create your views here.
from .models import Contact

def contact(request):
    contact = Contact.objects.first()
    return render(request,'contact/contact.html',context={'contact':contact})
