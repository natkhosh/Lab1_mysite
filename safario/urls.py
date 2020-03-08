from django.urls import path
from safario.views import *
from django.http import HttpResponse


def get_started(request):
    html = f"<html><body> Coming soon! </body></html>"
    return HttpResponse(html)


urlpatterns = [
    path('', SafarioView.as_view()),
    path('contact/', ContactsView.as_view()),
    path("getstarted/", get_started),
]

