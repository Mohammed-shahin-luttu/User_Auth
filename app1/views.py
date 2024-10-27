from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
# Create your views here.

@never_cache
@login_required(login_url='login')
def HomePage(request):
  if request.user.is_authenticated:
    return render(request,'home.html')
  return render(request, 'home.html')

# -----------------------------------------------------------------------------
@never_cache
def SignUpPage(request):
  if request.method == 'POST':
    uname = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if password1!=password2:
      return HttpResponse("your password and conform password are not same!!!")
    else:
      my_user = User.objects.create_user(uname,email,password1)
      my_user.save()
      return redirect('login')
    
  return render(request,'SignUp.html')

# -----------------------------------------------------------------------------

@never_cache
def LoginPage(request):
  if request.user.is_authenticated:
    return render(request,'home.html')
  error=''
  if request.method == 'POST':
    username = request.POST.get('username')
    pass1 = request.POST.get('pass')
    user = authenticate(request ,username=username ,password=pass1)
    if user is not None:
      login(request,user)
      return render(request,'home.html')
    else: 
      error = "username or password is incorrect"
      
  return render(request, 'login.html',{"message": error})
# -----------------------------------------------------------------------------

def LogoutPage(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      logout(request)
      return redirect('signup')
    return redirect('home',{"user":request.user.username})
  return render(request,'login.html')
      
    
        
  