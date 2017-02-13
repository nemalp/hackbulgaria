"""course_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from courses import views
from website import views as web_views

urlpatterns = [
    url(r'^$', views.all_courses, name='all_courses'),
    url(r'^admin/', admin.site.urls),
    url(r'^course/', include('courses.urls')),
    url(r'^lecture/', include('lectures.urls')),
    url(r'^register/', web_views.register, name='register'),
]
