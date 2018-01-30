from django.shortcuts import render, HttpResponse

from .models import Inscription


def students(request):
    inscriptions = Inscription.objects.all()
    context = {'inscriptions': inscriptions}
    return render(request, 'students/student-list.html', context)


# Student folder view
def student_folder(request, id):
    student = Inscription.objects.get(id=id)
    context = {'student': student}
    return render(request, 'students/student-folder.html', context)
