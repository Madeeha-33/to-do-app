from multiprocessing.util import is_abstract_socket_namespace
from django.shortcuts import render , redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request , f"Congratulations!!! {username} you have successfully registered")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request , 'users/register.html', {'form':form})
def logout_view(request):
    logout(request)
    return redirect('login')

