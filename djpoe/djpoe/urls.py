# djpoe/djpoe/urls.py
"""URL configuration for djpoe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/

Examples
--------
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls

urlpatterns = [
    # modified admin path to avoid conflict with wagtail
    path("django-admin/", admin.site.urls),
    # wagtail admin
    path("admin/", include(wagtailadmin_urls)),
    # django-allauth
    path("accounts/", include("allauth.urls")),
    # TODO: Put your app's urls here
    # Media and static files
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    *debug_toolbar_urls(),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    re_path(r"", include(wagtail_urls)),
]
