from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect


def get_page (request):
    #showhistory = History.objects.all()
    if request.method == 'GET':
        x = request.GET.get('num_x_get', '')
        op = request.GET.get('op_get', '')
        y = request.GET.get('num_y_get', '')
        if op == '+':
            result_get = int(x) + int(y)
        if op == '-':
            result_get = int(x) - int(y)
        if op == '*':
            result_get = int(x) * int(y)
        if op == '/':
            result_get = int(x) / int(y)
        else:
            result_get = 10101
        #history = History.objects.create(number1=x,operater=op,number2=y,result=result)
        #history.save()
        return render(request,'homeget.html',{'result': result_get})

    else:
        result_get = 0
        return render(request,'homeget.html',{'result': result_get,})

