from django.urls import path
from . import views
from .views import HomeView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
