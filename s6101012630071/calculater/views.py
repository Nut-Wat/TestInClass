from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect



def home_page (request):
    return render(request,'home.html')