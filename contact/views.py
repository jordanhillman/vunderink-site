from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



# If request contains form input, send email and render success page. Otherwise, render contact page.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Website Inquiry"
            body = {
                'mail': form.cleaned_data['email'],
                'sub': form.cleaned_data['subject'],
                'mes': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'jordanhillman@gmail.com',['jordanhillman@gmail.com'])
            except BadHeaderError:
                return HttpResponse('invalid header found')
            return render(request, 'contact/success.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
