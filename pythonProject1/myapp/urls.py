from django.urls import path
from .views import index_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index_view, name='index_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)