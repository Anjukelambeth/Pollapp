from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Account

from accounts.forms import RegistrationForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'home')
            return redirect('/')
        else:
            messages.error(request, "Username Or Password is incorrect!",
                           extra_tags='alert alert-warning alert-dismissible fade show')

    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def create_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name= form.cleaned_data['first_name']
            last_name= form.cleaned_data['last_name']
            password= form.cleaned_data['password']
            
            email = form.cleaned_data['email']
            phone_number=form.cleaned_data['phone_number']
            username=email.split("@")[0]
            user= Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password,phone_number=phone_number,user_name=username)
            user.save()
            messages.success(
                request, f'Thanks for registering {user.first_name}.', extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('accounts:login')
        
                
        else:
            print(form.errors) 
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})