# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import UserLoginForm
from django.template import RequestContext
from django.contrib.auth import login
from django.template.response import TemplateResponse

def login(request):
    
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            login(request, user_form.get_user())
            return HttpResponseRedirect('/compose/')

    else:
        login_form = UserLoginForm()

    context_login = { 'login_form' : login_form }

    return TemplateResponse(request, 'login_form.html', context_login)
    # return RequestContext(request, context_login)
