from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from io import BytesIO

from reportlab.pdfgen import canvas

from .forms import PayementForm, FeeForm
from .models import Payement, Fees


@login_required
def payement(request):
    return render(request, 'payement/payement.html')


@login_required
def new_payement(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="receipt.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PayementForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            # form.save()
            # return redirect('payement')

            # Draw things on the PDF. Here's where the PDF generation happens.
            # See the ReportLab documentation for the full list of functionality.
            p.drawString(100,800 , "Hello world.")

            # Close the PDF object cleanly.
            p.showPage()
            p.save()

            # Get the value of the BytesIO buffer and write it to the response.
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response
    else:
        form = PayementForm()
    context = {'form': form}
    return render(request, 'payement/new-payement.html', context)


@login_required
def fees(request):
    fees = Fees.objects.all()
    return render(request, 'payement/fees.html', { 'fees': fees })


@login_required
def new_fee(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FeeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save(commit=True)
            return redirect('fees')
    else:
        form = FeeForm()
    context = {'form': form}
    return render(request, 'payement/new-fee.html', context)


@login_required
def edit_fee(request, fee_id):
    fee = get_object_or_404(Fees, id=fee_id)
    if request.POST:
        form = FeeForm(data=request.POST, instance=fee)
        if form.is_valid():
            form.save()
            return redirect('fees')
    else:
        form = FeeForm(instance=fee)
    return render(request, 'payement/new-fee.html',
        {'form': form, 'fee': fee})


@login_required
def delete_fee(request, pk):
    data = dict()
    fee = get_object_or_404(Fees, pk=pk)
    if request.method == 'POST':
        fee.delete()
        return redirect('fees')
    else:
        context ={'fee': fee}
        data['html_form'] = render_to_string('payement/partial-fee-delete.html',
            context, request=request)
    return JsonResponse(data)