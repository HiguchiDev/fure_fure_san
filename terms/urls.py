from django.urls import path
from . import views
from .views import HomeView
from django.conf import settings
from django.conf.urls.static import static

# このファイルは不要？

urlpatterns = [
    path('terms/', HomeView.as_view(), name='terms'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
