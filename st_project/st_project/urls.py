"""st_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from os import stat
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from st_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help.html', views.help, name='help'),
    path('admin/', admin.site.urls),
    path('nform/', views.get_degree, name='nform'),
    path('nform2/', views.get_student, name='nform2'),
    path("result_search/", views.SearchResultsView.as_view(), name= "result_search"),
    path("form_search/", views.output, name="form_search"),
]