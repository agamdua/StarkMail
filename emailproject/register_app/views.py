# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.template.response import TemplateResponse

from .forms import UserCreateForm

# TODO: use the require post
def post(request):

    form = UserCreateForm(request.POST)

    if form.is_valid():

        cleaned_data = form.cleaned_data
        username = cleaned_data['username']
        password = cleaned_data['password']
        form.save(commit=True)
        user = authenticate(username=username, password=password)
        login(request, user)

        # TODO: use reverse over here
        return HttpResponseRedirect('/compose/')

    
    context_register = {
        'form' : form,
    }

    return TemplateResponse(request, 'register_form.html', context_register)
    # return RequestContext(request, context_register)

