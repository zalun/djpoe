"""Models for the home app."""

# djpoe/home/models.py
from typing import ClassVar

from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class HomePage(Page):
    """Home page model."""

    body = RichTextField(blank=True)

    content_panels: ClassVar[list[FieldPanel]] = [*Page.content_panels, FieldPanel("body")]
