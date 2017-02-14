from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from base_app.models import User
import ipdb


def register(request):
    # TODO implement decorator for checking if user is logged
    if request.session.get('email'):
        return redirect('/profile/')

    if request.method == 'POST':
        email = request.POST['email']
        passw = request.POST['password']

        ipdb.set_trace()
        if not User.exists(email):
            User(email=email, password=passw).save()
            # TODO redirect to profile

    return render(request, 'auth/register.html', locals())


def login(request):
    # TODO implement decorator for checking if user is logged
    if request.session.get('email'):
        return redirect('/profile/')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if User.login(email, password):
            request.session['email'] = email
            return redirect('/profile/')
        else:
            error_msg = 'Invalid username or password'

    return render(request, 'auth/login.html', locals())


def profile(request):
    # TODO implement decorator for checking if user is logged
    if not request.session.get('email'):
        return redirect('/login/')

    return render(request, 'partials/profile.html')
