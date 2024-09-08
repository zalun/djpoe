# djpoe/helloworld/views.py
"""Views for the helloworld app."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """Return a simple greeting."""
    return render(request, "helloworld/index.html")
