# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.template.response import TemplateResponse

from .forms import UserLoginForm


#TODO: Use the require post decorator
def login_view(request):
    
    form = UserLoginForm(request=request, data=request.POST)

    if form.is_valid():
        login(request, request.user)

        # TODO: Use reverser over here
        return HttpResponseRedirect('/compose/')
        
    context = { 
        'form': form 
    }

    return render(request, 'login_form.html', context)

def logout_view(request):

    logout(request)

    # TODO: Use reverser over here
    return HttpResponseRedirect('/login/')
