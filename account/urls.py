from django.urls import path

from account.views import send_mail


urlpatterns = [
    path('hello/', send_mail),
]