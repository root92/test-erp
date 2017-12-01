from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    if request.user.is_authenticated():
        return home(request)
    else:
        return render(request, 'core/login.html')

@login_required
def home(request):
    return render(request, 'core/home.html')



