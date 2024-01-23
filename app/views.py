from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail

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