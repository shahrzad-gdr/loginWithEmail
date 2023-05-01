from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from account.forms import LoginForm
import logging


def index(request):
    return render(request,'account/index.html')



def user_login(request):
    global user
    title = 'login page'
    login_form = LoginForm()

    if request.method == 'POST':
        email= request.POST.get('email')
        password= request.POST.get('password')
        remember_me= request.POST.get('remember_me')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)  # Here if the remember me is False, that is why expiry is set to 0 seconds. So it will automatically close the session after the browser is closed.
                return redirect('index')
            else:
                messages.error(request, 'This account is not active', 'warning')
        else:
            messages.error(request, 'Invalid email or password', 'danger')

    context = {
        'title' : title,
        'form' : login_form,
    }
    return render(request, 'account/login.html', context)

