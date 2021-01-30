from django.shortcuts import render, redirect
from .models import *
from .forms import UnivercityForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


@login_required
def home(request):
    universitis = University.objects.all()
    form = UnivercityForm()
    if request.method == "POST":
        form = UnivercityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    
    context = {'universitis':universitis,'form':form}
    return render(request,'home.html',context)

@login_required
def detail(request, pk):
    universitis = University.objects.get(id=pk)
    return render(request,'detail.html', {"uni":universitis})

@login_required
def delete(request,pk):
    item = University.objects.get(id=pk)
    item.delete()
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {
        'form': form
    })