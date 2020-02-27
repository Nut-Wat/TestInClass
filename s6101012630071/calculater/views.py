from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from calculater.models import History


def home_page (request):
    showhistory = History.objects.all()
    if request.method == 'POST':
        x = request.POST.get('num_x', '')
        op = request.POST.get('op', '')
        y = request.POST.get('num_y', '')
        if op == '+':
            result = int(x) + int(y)
        if op == '-':
            result = int(x) - int(y)
        if op == '*':
            result = int(x) * int(y)
        if op == '/':
            result = int(x) / int(y)
        history = History.objects.create(number1=x,operater=op,number2=y,result=result)
        history.save()
        return render(request,'home.html',{'result': result,'showhistory':showhistory})

    else:
        result = 0
        return render(request,'home.html',{'result': result,'showhistory':showhistory,})

