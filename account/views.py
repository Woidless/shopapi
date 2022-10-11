from django.shortcuts import render
from django.http import HttpResponse
from .send_email import send_confirmation_email


def send_mail(request):
    html = "<html><body>Hello your gmail</body></html>"
    send_confirmation_email('abdb2226@gmail.com', '1234')
    return HttpResponse(html)