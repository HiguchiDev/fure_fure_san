"""fure_fure_san URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
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
from django.contrib import admin
from django.urls import path, include
from five.views import Index
from rest_framework import routers
from top.views import AnswerViewSet, TopPageView



defaultRouter = routers.DefaultRouter()
defaultRouter.register('answer',AnswerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('top/', TopPageView.as_view()),
    # defaultRouter をinclude する
    path('api/',include(defaultRouter.urls)),
    path('five/', Index.as_view()),
]
