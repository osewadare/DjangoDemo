from django.shortcuts import render
from .models import Student
from .forms import StudentForm

def indexview(request):
    return render(request, 'demoapp/index.html')

def listview(request):
    students = Student.objects.all()
    context = {'students' : students}
    return render(request, 'demoapp/list.html', context)


def createStudent(request):
    submitted = False
    if request.method == 'POST':
        student_form = StudentForm(data=request.POST)
        if student_form.is_valid():
            student_form.save()
            submitted = True
    else:  #else request is GET
        student_form = StudentForm()
    context = {'student_form': student_form, 'submitted': submitted}
    return render(request, 'demoapp/add.html', context)

