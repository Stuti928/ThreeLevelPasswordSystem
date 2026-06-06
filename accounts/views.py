from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserData


def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        rgb_password = request.POST.get('rgb_password')
        image_password = request.FILES.get('image_password')

        UserData.objects.create(
            username=username,
            email=email,
            password=password,
            rgb_password=rgb_password,
            image_password=image_password
        )

        messages.success(request, "Registration Successful! Please log in.")

        return redirect('/register/')

    return render(request, 'register.html')


def login(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        try:

            user = UserData.objects.get(
                email=email,
                password=password
            )

            request.session['user_id'] = user.id

            return redirect('/rgb/')

        except UserData.DoesNotExist:

            return render(
                request,
                'login.html',
                {'error': 'Invalid Email or Password'}
            )

    return render(request, 'login.html')


def rgb_auth(request):

    if request.method == 'POST':

        rgb_password = request.POST.get('rgb_password')

        user_id = request.session.get('user_id')

        user = UserData.objects.get(id=user_id)

        if user.rgb_password == rgb_password:

            return redirect('/image-auth/')

        else:

            return render(
                request,
                'rgb_auth.html',
                {'error': 'Wrong RGB Password'}
            )

    return render(request, 'rgb_auth.html')


def image_auth(request):

    if request.method == 'POST':

        image_code = request.POST.get('image_code')

        if image_code == "1234":

            return redirect('/dashboard/')

        else:

            return render(
                request,
                'image_auth.html',
                {'error': 'Wrong Image Password'}
            )

    return render(request, 'image_auth.html')


def dashboard(request):
    return render(request, 'dashboard.html')