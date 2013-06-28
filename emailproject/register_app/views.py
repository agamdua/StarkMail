# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from forms import UserCreateForm
from django.template import RequestContext

def post(request):

    user_form = UserCreateForm(request.POST)
    
    if user_form.is_valid():
        username = user_form.clean_username()
        password = user.form.clean_password2()
        user_form.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect('/compose/')

    else:
        user_form = UserCreateForm()

    return render_to_response('base.html', {
        'user_form' : user_form },
        context_instance=RequestContext(request))

