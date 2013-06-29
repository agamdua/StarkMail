from django.shortcuts import render
from register_app.views import post 

def home(request):
    return post(request)
    # return render(request, 'base.html') 
