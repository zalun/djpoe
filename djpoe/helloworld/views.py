# djpoe/helloworld/views.py
"""Views for the helloworld app."""

from django.http import HttpRequest, HttpResponse


def index(_: HttpRequest) -> HttpResponse:
    """Return a simple greeting."""
    return HttpResponse("Hello, World!")
