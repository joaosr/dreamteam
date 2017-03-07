from django.shortcuts import render
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from dreamteam.settings import EMAIL_HOST_USER
from dreamteam.settings import BASE_URL

# Create your views here.

def send_confirmation_email(email, token):
    subject = "Thank for sign up to DreemTeam"
    link = reverse('api:confirmation_email', kwargs={'token':token})
    link = BASE_URL+link
    a = "<a href='{}'>{}</a>".format(link,link)
    message = "Welcome to DreamTeam!<br/> <br/> Click the link below to verify your email address:<br/><br/><br/>"+a
    from_mail = EMAIL_HOST_USER
    _list = [email,]

    # msg = EmailMultiAlternatives(subject, message, from_mail, _list, fail_silently=False)
    msg = EmailMultiAlternatives(subject, message, from_mail, _list)
    msg.attach_alternative(message, "text/html")
    msg.send()
    return 1
