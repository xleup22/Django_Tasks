from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import user
from .models import enquiry
from django.contrib import messages
from django.contrib.auth import authenticate, login
 
from django.template import loader
 
# Create your views here.
def home(request):
        return render(request, 'myApp/home.html')
def about(request):
        return render(request, 'myApp/about.html')
def contact(request):
        return render(request, 'myApp/contact.html')
def signin(request):
        return render(request, 'myApp/signin.html')
def password(request):
        return render(request, 'myApp/password.html')
""" def profile(request):
        return render(request, 'myApp/profile.html') """
def reg(request):
        return render(request, 'myApp/reg.html')
def smartphone(request):
        return render(request, 'myApp/smartphone.html')
def smartwatch(request):
        return render(request, 'myApp/smartwatch.html')
def television(request):
        return render(request, 'myApp/television.html')
def product1(request):
        return render(request, 'myApp/product1.html')
def product2(request):
        return render(request, 'myApp/product2.html')
def product3(request):
        return render(request, 'myApp/product3.html')
def reg(request):
            if request.method == 'POST':
             if request.POST.get('FirstName') and request.POST.get('LastName'):
                post=user()
                post.FirstName= request.POST.get('FirstName')
                post.LastName= request.POST.get('LastName')
                post.DOB= request.POST.get('DOB')
                post.Phone= request.POST.get('Phone')
                post.email= request.POST.get('email')
                post.Address= request.POST.get('Address')
                post.City= request.POST.get('City')
                post.Country= request.POST.get('Country')
                post.ZipCode= request.POST.get('ZipCode')
                post.Password= request.POST.get('Password')
                    
                post.save()
                messages.success(request, "Your account has been created successfully.")
                return render(request, 'myApp/signin.html')
            else:
                return render(request,'myApp/reg.html')
            
def contact(request):
            if request.method == 'POST':
             if request.POST.get('FirstName') and request.POST.get('LastName'):
                post=enquiry()
                post.FirstName= request.POST.get('FirstName')
                post.LastName= request.POST.get('LastName')
                post.Email= request.POST.get('Email')
                post.PhoneNumber= request.POST.get('PhoneNumber')
                post.Message= request.POST.get('Message')
                                    
                post.save()
                return render(request, 'myApp/contact.html')
            else:
                return render(request,'myApp/contact.html')
            
def signin(request):
            if request.method == 'POST':
                username= request.POST['username']
                password= request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None: 
                       login(request,user)
                       return redirect('home')
                #        return render(request, 'myApp/profile.html')
                                            
                else:
                       messages.error(request, "Bad credentials!")
                       return render(request,'myApp/signin.html')
            else:   
                return render(request,'myApp/signin.html')

           


            


       

               
        



