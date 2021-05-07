from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    return render(request,'Upload_App/index.html',context={})