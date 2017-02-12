from django.shortcuts import render, redirect
from lectures.models import Lecture
from courses.models import Course


def new_lecture(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        course_name = request.POST.get('course_name')
        course = Course.objects.get(name=course_name)
        week = int(request.POST.get('week'))
        url = request.POST.get('url')

        Lecture.objects.create(name=name, week=week,
                               course=course, url=url)
        lecture_id = Lecture.objects.get(name=name).id

        return redirect('/lecture/{}'.format(lecture_id))

    return render(request, 'new_lecture.html', locals())


def edit_lecture(request, lecture_id):
    courses = Course.objects.all()
    lecture = Lecture.objects.get(id=int(lecture_id))

    if request.method == 'POST':
        lecture.name = request.POST.get('name')
        course_name = request.POST.get('course_name')
        lecture.course = Course.objects.get(name=course_name)
        lecture.week = int(request.POST.get('week'))
        lecture.url = request.POST.get('url')

        lecture.save()

        return redirect('/lecture/{}'.format(lecture.id))

    return render(request, 'edit_lecture.html', locals())


def lecture_details(request, lecture_id):
    lecture = Lecture.objects.get(id=lecture_id)

    return render(request, 'lecture_details.html', locals())
