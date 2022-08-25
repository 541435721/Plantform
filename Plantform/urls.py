"""Plantform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
import MicroApp.views as views
from django.views.static import serve
from . import settings

urlpatterns = [
    #    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^test_db$', views.testDB, name='testDB'),
    url(r'^login$', views.user_login, name='login'),
    url(r'^register$', views.user_register, name='register'),
    url(r'^manage$', views.manager, name='manage'),
    url(r'^detail$', views.detail, name='detail'),
    url(r'^create_proj$', views.create_proj, name='create_proj'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^chart$', views.chart, name='chart'),

    url(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
]
