from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from misitioweb.settings import EMAIL_HOST_USER
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #Enviar email y redireccionar
            email = EmailMessage(
                subject=f"Nuevo mensaje de {cd['name']} - {cd['email']}",
                body=cd['mensaje'],
                from_email=EMAIL_HOST_USER,
                to=['inigo.pa@icjardin.com'],
                reply_to=[cd['email']]
            )
            try:
                email.send()
                return redirect(reverse("contact") + "?ok")
            except:
                return redirect(reverse("contact") + "?fail")
            
        else:
            contact_form = ContactForm()
            return render(request, "contact/contact.html", {'form': contact_form})
        
    contact_form = ContactForm()
    return render(request, "contact/contact.html", {'form': contact_form})
