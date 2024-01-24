from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.urls import reverse

def registration(request):
    ufo = UserForm()
    pfo = ProfileForm()
    d = {'ufo':ufo,'pfo':pfo}
    if request.method == 'POST' and request.FILES :
        ufd = UserForm(request.POST)
        pfd = ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            MUFDO = ufd.save(commit = False)
            pw = ufd.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO = pfd.save(commit = False)
            MPFDO.username = MUFDO
            MPFDO.save()

            send_mail(
                'Registration',
                'Registration is Successful',
                'sreenugattu5@gmail.com',
                [MUFDO.email],
                fail_silently=False
            )

            return HttpResponse('Registration is successful')
        else:
            return HttpResponse('Invalid data..')

    return render(request,'registration.html',d)

def home(request):
    if request.session.get('username'):
        username = request.session.get('username')
        d = {'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['un']
        password = request.POST['pw']
        # Now authenticate the user
        # so from django.contrib.auth import authenticate,login

        AUO = authenticate(username = username,password = password)
        if AUO and AUO.is_active:  # If user is valid and he is active
            login(request,AUO)      # creating login request
            request.session['username'] = username      # creating sessions

            return HttpResponseRedirect(reverse('home')) # hold the login req,session and auo. Now redirect to Home function
        else:
            return HttpResponse('Invalid Credentials')
    return render(request,'user_login.html')


