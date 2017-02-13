from django.conf.urls import url
from website import views


urlpatterns = [
    url(r'^register', views.register, name='register'),
]
