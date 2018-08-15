from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


from django.urls import reverse


#----------------to signup view -------------------
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
#------------------------------------------------

# Create your views here.

def login1(request):
	return render(request,'manage_cookies/login1.html')

def page1(request):
	return render(request,'manage_cookies/page1.html')

def page2(request):
	return render(request,'manage_cookies/page2.html')

def loginCookie(request):
	return render(request,'manage_cookies/login_cookie.html')

#view for signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login1')
    else:
        form = SignUpForm()
    return render(request, 'manage_cookies/signup.html', {'form': form})