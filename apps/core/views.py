from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    if request.user.is_authenticated():
        return home(request)
    else:
        return render(request, 'core/login.html')


@login_required
def home(request):
    return render(request, 'core/home.html')
