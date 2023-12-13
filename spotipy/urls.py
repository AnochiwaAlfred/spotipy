
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve
from apis.api import api as api
from apis.v1.clientAuth import google_authenticate
# from django.conf.urls import url
from dashboard.admin import DASHBOARD

VERSION = "v1"

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # DASHBOARD URLS
    path("spotipy/", DASHBOARD.urls, name='spotipy'),
    # path("dashboard/{app}/", dashboard.urls, name='dashboard-app'),
    # path("dashboard/{app}/{model}/", dashboard.urls, name='dashboard-model'),
    
    path(f"api/{VERSION}/", api.urls),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    # re_path(r'^auth/', include('social_django.urls', namespace='social')),
    path('auth/google/', google_authenticate, name='google-oauth2'),
    path('auth/', include('social_django.urls', namespace='social')),
    # url(r'^auth/', include('social_django.urls', namespace='social')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)