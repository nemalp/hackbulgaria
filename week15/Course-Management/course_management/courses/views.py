from django.shortcuts import render, redirect
from courses.models import Course
import ipdb


def course_details(request, *args, **kwargs):
    courses = Course.objects.all()
    return render(request, 'course_details.html', locals())


def create_course(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST.get('name')

        # ipdb.set_trace()
        if Course.objects.filter(name=name).exists():
            course = True
            return render(request, 'create_course.html', locals())

        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        Course.objects.create(name=name, description=description, 
                              start_date=start_date, end_date=end_date)

        return redirect('/')

    return render(request, 'create_course.html', locals())
