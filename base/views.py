#from email import message
from ast import Assign
#from msilib.schema import CheckBox
from optparse import check_choice
from pickle import NONE
from typing import Any,Text,Dict,List
from unittest import result
from django.contrib import messages
#from .models import National, School
from multiprocessing import context
from urllib import request
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import County, National
from .models import ExtraCounty
from .models import School


# Create your views here.

#login Function
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'user does not exist Create a user')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
           messages.error(request,'username Or password does not exist')
    context={}
    return render(request,'login.html',context)

#Logout Function
def logoutUser(request):
    logout(request)
    return redirect('home')

#home queryset 
def home(request):
    school_list = School.objects.all()
    context = {'school_list': school_list}
    return render(request, 'home.html', context)

# #School Template
def school(request, pk):
    school= School.objects.get(id=pk)
    context = {'school': school}
    return render(request,'school.html', context)

#getting schools from database
#def national(request):
    #national = National.objects.all()
    #context = {'national':national}
    #return render(request,'school.html',context)

#Registration Function with UserCreationForm
def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'An error occurred during registration')
    return render(request, 'register.html',{'form':form})




#submit button
def submit_result(request):
     form = UserCreationForm(request.POST)
     if request.methond =='POST':
         if form.is_valid():
             submit = form.save(commit=False)
             submit.save()
             return redirect('home')


#update button
def update_result(request):
     form = update_result(request.POST)
     if request.methond =='POST':
         if form.is_valid():
             submit = form.save(commit=False)
             submit.save()
             return redirect('home')


