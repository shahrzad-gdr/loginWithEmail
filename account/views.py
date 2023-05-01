from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from account.forms import LoginForm


def index(request):
    return render(request,'account/index.html')

