from django.shortcuts import render


def course_details(request, *args, **kwargs):
    return render(request, 'course_details.html', locals())


def create_course(request):
    pass
