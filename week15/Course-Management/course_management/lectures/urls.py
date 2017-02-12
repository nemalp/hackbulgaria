from django.conf.urls import url
from lectures import views

urlpatterns = [
    url(r'^new/$', views.new_lecture, name='new_lecture'),
    url(r'^edit/(?P<lecture_id>[\d]+)/$',
        views.edit_lecture, name='edit_lecture'),
    url(r'^(?P<lecture_id>[\d]+)/$',
        views.lecture_details, name='lecture_details'),
]
