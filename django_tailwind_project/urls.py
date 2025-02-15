"""
URL configuration for django_tailwind_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.templatetags.static import static
from django.shortcuts import render
from django.urls import path
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


class Demo1View(TemplateView):
    template_name = 'demo1.html'


class Demo2View(TemplateView):
    template_name = 'demo2.html'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('demo-1', Demo1View.as_view(), name='demo_1'),
    path('demo-2', Demo2View.as_view(), name='demo_2'),
]
