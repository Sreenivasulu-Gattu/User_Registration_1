from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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

# login decorator is required for logout 
# so from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def display_profile(request):
    un = request.session.get('username')
    uo = User.objects.get(username = un)
    po = Profile.objects.get(username = uo)
    d = {'uo':uo,'po':po}
    return render(request,'display_profile.html',d)

@login_required
def change_password(request):
    if request.method == 'POST':    
        username = request.session.get('username')
        UO = User.objects.get(username = username)
        password = request.POST['pw']
        UO.set_password(password)
        UO.save()
        return HttpResponse('Password Changed Successfully')
    return render(request,'change_password.html')

def forgot_password(request):
    if request.method == 'POST':
        username = request.POST['un']
        LUO = User.objects.filter(username = username)
        if LUO:
            UO = LUO[0]
            pw = request.POST['pw']
            UO.set_password(pw)
            UO.save()
            return HttpResponse('Reset Password Successful')
    return render(request,'forgot_password.html')

