# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import UserLoginForm
from django.contrib.auth import login, logout, authenticate
from django.template.response import TemplateResponse

def login_view(request):
    
    if request.method == 'POST':
        login_form = UserLoginForm(request=request, data=request.POST)

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        # set_password(password)

        user = authenticate(username=username, password=password)

        if login_form.is_valid:
            login(request, user)
            return HttpResponseRedirect('/compose/')
            
        # else:
        #     return HttpResponseRedirect('/')


    else:
        login_form = UserLoginForm()


    context_login = { 'login_form' : login_form }

    return TemplateResponse(request, 'login_form.html', context_login)
    # return RequestContext(request, context_login)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')