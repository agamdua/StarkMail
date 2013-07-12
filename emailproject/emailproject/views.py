from django.shortcuts import render

from login_app.forms import UserLoginForm
from register_app.forms import UserCreateForm

def home(request):


    context = {
        'login_form': UserLoginForm(),
        'register_form': UserCreateForm(),
    }

    return render(request, 'index.html', context)
