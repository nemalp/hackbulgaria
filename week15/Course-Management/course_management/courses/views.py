from django.shortcuts import render, redirect
from courses.models import Course
from lectures.models import Lecture
import ipdb


def all_courses(request, *args, **kwargs):
    courses = Course.objects.all().order_by('start_date')
    return render(request, 'all_courses.html', locals())


def create_course(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST.get('name')

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


# why is it not working when passing course_name as function parameter?
def edit_course(request, *args, **kwargs):
    course_name = kwargs.get('course')
    course = Course.objects.get(name=course_name)

    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.description = request.POST.get('description')
        course.start_date = request.POST.get('start_date')
        course.end_date = request.POST.get('end_date')

        course.save()

        return redirect('/course/{}'.format(course_name))

    return render(request, 'edit_course.html', locals())


def course_details(request, *args, **kwargs):
    course_name = kwargs.get('course_name')
    course = Course.objects.get(name=course_name)
    if Lecture.objects.filter(course=course).all().exists():
        lectures = Lecture.objects.filter(course=course).all()

    return render(request, 'course_details.html', locals())
