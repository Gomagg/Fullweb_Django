from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request, 'index.html')
  
def register(request):
  
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    
    if password == password2:
      if User.object.filter(email=email).exists():
        messages.info(request, 'Email Taken')
        return redirect('register')
      elif User.objects.filter(username=username).exists():
        messages.info(request, 'Username Taken')
        return redirect('register')
      else:
        User = User.objects.create_user(username=username, email=email, password=password)
        User.save();
        return redirect('login')
    else:
      messages.info(request, 'Password Not Matching')
      return redirect('register')
    return redirect ('/')
  else:
    return render(request, 'signup.html')
    
def login(request):
  return render(request, 'login.html')