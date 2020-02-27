from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from calculater.models import History

def home_page (request):
    return render(request,'home.html')

def me_page (request):
    return render(request,'me.html')


def calpost_page (request):
    showhistory = History.objects.all()
    if request.method == 'POST':
        if 'conti' in request.POST :
            con_num = request.POST.get('num_y', '')
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
            con_num = result
            return render(request,'calculaterpost.html',{'result': result,'showhistory':showhistory,'x':x,'y':y,'op':op,'con_num':con_num})
        else:
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
            return render(request,'calculaterpost.html',{'result': result,'showhistory':showhistory,'x':x,'y':y,'op':op})



    else:
        result = 0
        return render(request,'calculaterpost.html',{'result': result,'showhistory':showhistory})

