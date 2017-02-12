from django.conf.urls import url
from courses import views

urlpatterns = [
    url(r'^new/$', views.create_course, name='create_course'),
    url(r'^edit/(?P<course>[a-zA-Z\d\s]+)/$',
        views.edit_course, name='edit_course'),
    url(r'(?P<course_name>[a-zA-Z\d\s]+)/$',
        views.course_details, name='course_details')

]
