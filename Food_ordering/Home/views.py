from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth import login, authenticate,logout
from django.views.decorators.csrf import csrf_exempt
from urllib import request

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from Home.models import payment

# Create your views here.

def index(request):
    return render(request,'index.html')

def offer(request):
    return render(request,'offer.html')

def order(request):
    return render(request,'order.html')

def payment(request):
    # if request.method == 'POST':
    #     # food = request.POST.get('food')
    #     Idno = request.POST.get('Idno')
    #     Date = request.POST.get('Date')
    #     Status = request.POST.get('Status')
    #     # print(food)
    #     food = "Southh Food"
    #     Payment =payment(Idno=Idno,Date=Date,Status=Status)
    #     Payment.save()
    #     return redirect('payment')
    # else:
        return render(request,'payment.html')

    # return render(request,'payment.html')

def swiggy(request):
    return render(request,'swiggy.html')

def admin_index(request):
    return render(request,'admin_index.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password) 
        print(user)
        if user is not None:
            login(request, user)
            return redirect('admin_index')
        else:
            return redirect('/login')
    else:
        return render(request, 'login.html')
    
def admin_panda(request):
    return render(request,'admin_panda.html')

def admin_swigy(request):
    return render(request,'admin_swigy.html')

def admin_zomat(request):
    return render(request,'admin_zomat.html')