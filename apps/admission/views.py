from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.views.generic.edit import UpdateView

from apps.school.models import ActiveAcademicYear
from apps.students.models import Payement
from .models import Registration, Inscription, AdmissionProcess
from .forms import RegistrationForm, InscriptionForm, AdmissionProcessForm

# Create your views here.
@login_required
def home_admission(request):
    
    return render(request, 'admission/home_reg.html')

#Implementing Registration process
@login_required
def registration(request):

    admissionProcess = AdmissionProcess.objects.all()
    registrations = Registration.objects.all()
    decision = Registration.process_registree
    context =  {'registrations':registrations, 'decision':decision}
    
    return render(request, 'admission/registration.html', context)

# implementing Registration form
@login_required
def new_registration(request):

    # Checking for the existence of the active year. Useful for new database
    try:
       active_year = ActiveAcademicYear.objects.last().academic_year.label
    except ActiveAcademicYear.DoestNotExists:
        active_year = None

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(data=request.POST, files=request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save(commit=True)
            return redirect('registration')
    else:
        form = RegistrationForm(initial={'active_year': active_year})

    return render(request, 'admission/new-registration.html', {'form': form})


# implementing Registration detail page
@login_required
def registration_detail(request, registration_id):
    registration = Registration.objects.get(id=registration_id)
    return render(request, 'admission/registration-detail.html', {'registration': registration})

# Update Registree profile
@login_required
def edit_registration(request, registration_id):
    registration = Registration.objects.get(id=registration_id)
    if request.POST:
        form = RegistrationForm(data=request.POST, files=request.FILES, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('registration')
    else:
        form = RegistrationForm(instance=registration)

    return render(request, 'admission/edit-registration.html', {'form': form, 'registration': registration})


#Delete Regitstree
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

# implement admission process list
@login_required
def admission_process(request):
    
    adprocess = AdmissionProcess.objects.all()
    payements = Payement.objects.all()
    context =  {'adprocess': adprocess, 'payement': payements}
    
    return render(request, 'admission/admission-process.html', context)


@login_required
def new_admission_process(request, id):
    #Fetch for the required Registree
    try:
        registration = Registration.objects.get(id=id)
    except ActiveAcademicYear.DoestNotExists:
        registration = None
    
    registree = registration.id
    registree_number = registration.registry_number
    registree_name = registration

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AdmissionProcessForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            process = form.save(commit=False)
            process.user = request.user
            form.save()
            return redirect('registration')
    else:
        form = AdmissionProcessForm(initial={'registree_name':registree_name, 'registree_number':registree_number,
                                                'registree': registree})
    context = {'form': form, 'registree': registree, 'registree_number': registree_number,
                'registree_name':registree_name, 'registration': registration}
    return render(request, 'admission/new-process.html', context)


# Implement inscription
@login_required
def new_inscription(request, id):

    try:
       active_year = ActiveAcademicYear.objects.last().academic_year.id
    except ActiveAcademicYear.DoestNotExists:
        active_year = None
    registration = Registration.objects.get(id=id)
    reg_payement = registration.registration_payement.all()
    registree = registration.id
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InscriptionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            process = form.save(commit=False)
            process.user = request.user
            form.save()
            return redirect('admission-process')
    else:
        form = InscriptionForm(initial={'registry': registree, 'active_year': active_year})
    context = {'form': form, 'registration':registration, 'reg_payement': reg_payement}
    return render(request, 'admission/new-inscription.html', context)

@login_required
def admission(request):
    inscriptions = Inscription.objects.all()
    registree = registration.id
    return render(request, 'admission/admission.html', {'inscriptions': inscriptions})


@login_required
def new_admission(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        reg_form = AdmissionForm(data=request.POST, files=request.FILES)
        # check whether it's valid:
        if reg_form.is_valid():
            reg_form.save(commit=True)
            return redirect('admission')
    else:
        form = AdmissionForm()

    return render(request, 'admission/new-admission.html', {'form': form})


@login_required
def admission_detail(request, admission_id):
    admission = Admission.objects.get(id=admission_id)
    return render(request, 'admission/admission-detail.html', {'admission': admission})




# def confirm_admission(request, pk):
#     data = dict()
#     fee = AdmissionProcess.objects.get(pk=pk)
#     if request.method == 'POST':
#         # registration.delete()
#         # return redirect('registration')
#         print("cool")
#     else:
#         context ={'registration': registration}
#         data['html_form'] = render_to_string('admission/partial-registration-delete.html', context, request=request)
#         return JsonResponse(data)

