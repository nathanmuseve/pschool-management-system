from django.urls import path
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import settings
from django.conf.urls import static



urlpatterns = [
    path('', views.test, name='home'),
] + debug_toolbar_urls()

# urlpatterns = [
#     # other url patterns
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

