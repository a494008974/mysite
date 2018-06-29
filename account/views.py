from django.shortcuts import render
from django.contrib.auth import authenticate,login
from .forms import LoginForm
# Create your views here.

def index(request):
    return render(request,'account/index.html')


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return render(request,'account/login_success.html')
            else:
                return render(request, 'account/login_defeated.html')
        else:
            return render(request, 'account/login_defeated.html')
    elif request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'account/login.html',{'form':login_form})
