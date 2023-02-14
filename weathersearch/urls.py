"""weathersearch URL Configuration

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
from django.urls import path
from result import views as result_views

urlpatterns = [
    path('', result_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('about-us/', result_views.about, name='about'),
    path('previous-results/', result_views.previous_results, name='previous-results'),
    path('search/', result_views.search, name='search'),
    path('contact-us/', result_views.contact, name='contact'),
    path('save-result/', result_views.save_result, name='save-result'),
    path('message/', result_views.message, name='message'),
]

