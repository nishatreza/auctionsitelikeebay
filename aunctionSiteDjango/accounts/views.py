from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/')

    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                print('User created!')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching!')
            return redirect('register')
    else:
        return render(request, 'register.html')


# def logout(request):
#     auth.logout(request)
#     return redirect('/')
