from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from .forms import UserCreationForm
from .models import User
from django.contrib import messages

# Create your views here.
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
            context = {'name': request.POST.get('name', ''), 'email': request.POST.get('email', '')}
            return render(request, 'users/register.html', context)
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'users/register.html', context)
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password. Please try again.')
    return render(request, 'users/login.html')
 

def logout_view(request):
  logout(request)
  return redirect('login')
    

