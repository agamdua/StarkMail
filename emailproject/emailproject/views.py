from django.shortcuts import render
from register_app.views import post 
from login_app.views import login

def home(request):
    
    user_register = post(request)
    user_login = login(request)
     
    context_home = {
        'user_form' : user_form,
        'login_form' : login_form,
        }
        
    return render(request, 'base.html', context_home) 
