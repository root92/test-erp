from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home_admission(request):
    
    return render(request, 'admission/home_reg.html')