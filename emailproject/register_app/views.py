# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import UserCreateForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.template.response import TemplateResponse

def post(request):

    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
    
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/compose/')

    else:
        user_form = UserCreateForm()
    
    context_register = {
        'user_form' : user_form,
        }

    return TemplateResponse(request, 'register_form.html', context_register)
    # return RequestContext(request, context_register)

