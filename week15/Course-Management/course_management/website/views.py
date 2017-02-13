from django.shortcuts import render
from base_app.models import User
import ipdb


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        passw = request.POST['password']

        ipdb.set_trace()
        if not User.exists(email):
            User(email=email, password=passw).save()
            # TODO redirect to profile

    return render(request, 'auth/register.html', locals())


def login(request):
    return render(request, 'auth/register.html', locals())
