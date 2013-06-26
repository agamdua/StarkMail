# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import UserCreateForm

def post(self, request, *args, **kwargs):
    user_form = UserCreateForm(request.POST)
    if user_form.is_valid():
        username = user_form.clean_username()
        password = user.form.clean_password2()
        user_form.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect('/compose/')

    return render(request, 'base.html', {
        'user_form' : user_form })

