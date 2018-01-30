# from django.shortcuts import render
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render  # redirect, get_object_or_404 


# Create your views here.
@login_required
def dep_home(request):
    return render(request, 'department/dep_home.html')
            