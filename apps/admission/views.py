from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Registration, Admission
from .forms import RegistrationForm, AdmissionForm

# Create your views here.
@login_required
def home_admission(request):
    
    return render(request, 'admission/home_reg.html')

#Implementing Registration process
@login_required
def registration(request):

    registrations = Registration.objects.all()
    
    return render(request, 'admission/registration.html', {'registrations':registrations})

@login_required
def admission(request):
    
    return render(request, 'admission/admission.html')


@login_required
def newAdmission(request):
    
    return render(request, 'admission/newAdmission.html')


# implementing Registration form
@login_required
def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        reg_form = RegistrationForm(data=request.POST)
        # check whether it's valid:
        if reg_form.is_valid():
            reg_form.save(commit=True)
        return redirect('home')
    else:
        form = RegistrationForm()
        return render(request, 'admission/reg.html', {'form': form})