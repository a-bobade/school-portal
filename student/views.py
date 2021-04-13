from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def record(request):
    student = Student.objects.all()
    return render(request, 'record.html', {'student': student})


def search(request):
    query = request.GET.get('q')
    try:
        student = Student.objects.get(matric=query)
    except:
        messages.error(request, 'No Record Found')
        return redirect('/')
    return render(request, 'view.html', {'student': student})


def create(request):
    return render(request, 'create.html')


def store(request):
    student = Student()
    try:
        student.matric = request.POST.get('matric', False)
        student.fName = request.POST.get('fName', False)
        student.mName = request.POST.get('mName', False)
        student.lName = request.POST.get('lName', False)
        student.gender = request.POST.get('gender', False)
        student.dob = request.POST.get('dob', False)
        student.email = request.POST.get('email', False)
        student.course = request.POST.get('course', False)
        student.dept = request.POST.get('dept', False)
        student.faculty = request.POST.get('faculty', False)
        student.entry = request.POST.get('entry', False)
        student.exit = request.POST.get('exit', False)
        student.state = request.POST.get('state', False)
        student.save()
        messages.success(request, "Student Record Added Successfully")
    except:
        messages.error(request, 'Student Matric Number Already Exists')
    return redirect('/create')


def view(request, matric):
    student = Student.objects.get(matric=matric)
    return render(request, 'view.html', {'student': student})


def delete(request, matric):
    context = {}
    student = Student.objects.get(matric=matric)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student Deleted Successfully")
        return redirect('/')
    return render(request, "delete.html", context)


def updateStudent(request, matric):
    student = Student.objects.get(matric=matric)
    return render(request, 'update.html', {'student': student})


def update(request, matric):
    print('in')
    student = Student.objects.get(matric=matric)
    student.matric = request.POST.get('matric', False)
    student.fName = request.POST.get('fName', False)
    student.mName = request.POST.get('mName', False)
    student.lName = request.POST.get('lName', False)
    student.gender = request.POST.get('gender', False)
    student.dob = request.POST.get('dob', False)
    student.email = request.POST.get('email', False)
    student.course = request.POST.get('course', False)
    student.dept = request.POST.get('dept', False)
    student.faculty = request.POST.get('faculty', False)
    student.entry = request.POST.get('entry', False)
    student.exit = request.POST.get('exit', False)
    student.state = request.POST.get('state', False)
    student.save()
    messages.success(request, "Student Record Updated Successfully")
    return redirect('/')
