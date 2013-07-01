from django.shortcuts import render
from django.http import HttpResponse

from register_app.views import post 
from login_app.views import login

def home(request):
    
    user_form = post(request)
    user_form.render()
    login_form = login(request)
    login_form.render()

    context_home = {
        'user_form' : user_form.rendered_content,
        'login_form' : login_form.rendered_content,
        }
        
    return render(request, 'base.html', context_home) 
