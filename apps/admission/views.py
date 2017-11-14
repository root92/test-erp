from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string

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

# implementing Registration form
@login_required
def new_registration(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        reg_form = RegistrationForm(data=request.POST)
        # check whether it's valid:
        if reg_form.is_valid():
            reg_form.save(commit=True)
        return redirect('registration')
    else:
        form = RegistrationForm()
        return render(request, 'admission/new-registration.html', {'form': form})


# implementing Registration detai page
@login_required
def registration_detail(request, registration_id):
    registration = Registration.objects.get(id=registration_id)
    return render(request, 'admission/registration-detail.html', {'registration': registration})

@login_required
def edit_registration(request, registration_id):
    registration = Registration.objects.get(id=registration_id)

    if request.POST:
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('registration')
    else:
        form = RegistrationForm(instance=registration)
    return render(request, 'admission/edit-registration.html', {'form': form})


@login_required
def delete_registration(request, pk):
    data = dict()
    registration = Registration.objects.get(pk=pk)
    if request.method == 'POST':
        registration.delete()
        return redirect('registration')
    else:
        context ={'registration': registration}
        data['html_form'] = render_to_string('admission/partial-registration-delete.html', context, request=request)
        return JsonResponse(data)



@login_required
def admission(request):
    
    return render(request, 'admission/admission.html')


@login_required
def newAdmission(request):
    
    return render(request, 'admission/newAdmission.html')


