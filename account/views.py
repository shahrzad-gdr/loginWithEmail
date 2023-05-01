from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from account.forms import UserUpdateForm
from account.models import User


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request,'account/index.html')



def user_login(request):
    global user
    title = 'login page'
    if request.user.is_authenticated:
        return redirect('dashboard')


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
                return redirect('dashboard')
            else:
                messages.error(request, 'This account is not active', 'warning')
        else:
            messages.error(request, 'Invalid email or password', 'danger')

    context = {
        'title' : title,
    }
    return render(request, 'account/login.html', context)


@login_required()
def user_logout(request):
    logout(request)
    return redirect('index')




def user_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            try:
                user = User.objects.get(email=email)
                messages.error(request, 'invalid email', 'danger')
                return redirect('register')
            except:
                User.objects.create_user(
                    email=email,
                    password=password,
                )
                user = authenticate(email=email, password=password)
                login(request, user)
                return redirect('dashboard')
        else:
            messages.error(request, 'passwords does not match!', 'danger')
            return redirect('register')


    return render(request, 'account/register.html')


@login_required(login_url='index')
def dashboard(request):
    title = 'dashboard page'
    context = {
        'title' : title,
    }
    return render(request, 'account/dashboard.html', context)




@login_required(login_url='index')
def update(request):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST)
        try:
            if update_form.is_valid():
                cl_data = update_form.cleaned_data
                user = User.objects.get(id=request.user.id)
                user.first_name = cl_data['first_name']
                user.last_name = cl_data['last_name']
                user.save()
            messages.success(request, 'your profile updated successfully', 'success')

        except:
            messages.error(request, 'updating profile failed', 'danger')

    return redirect(url)
