from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Results


def resultForm(request):
    return render(request, 'result_form.html')


def save(request):
    result = Results()
    result.matric = request.POST.get('matric', False)
    result.code = request.POST.get('code', False)
    result.ca1 = request.POST.get('test1', False)
    result.ca2 = request.POST.get('test2', False)
    result.exam = request.POST.get('exam', False)
    result.mark = request.POST.get('mark', False)
    result.level = request.POST.get('level', False)
    result.semester = request.POST.get('semester', False)
    result.session = request.POST.get('session', False)
    result.trials = request.POST.get('trial', False)
    result.save()
    messages.success(request, "Student Result Uploaded Successfully")
    return redirect('/result-form')


def viewResult(request,):
    return render(request, 'result_check.html')


def searchResult(request):
    query = request.GET.get('result')
    result = Results.objects.filter(matric=query)
    return render(request, 'result_view.html', {'result': result})
