from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect



def home_page (request):
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
        return render(request,'home.html',{'result': result})

    else:
        result = 0
        return render(request,'home.html',{'result': result})

