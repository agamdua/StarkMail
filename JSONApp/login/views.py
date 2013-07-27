# Create your views here.

def login_view():
	if request.method=='POST':
			login_form=UserLoginForm(request=request, data=request.POST)

			username=resquest.POST.get('username' , '')
			password=resquest.POST.get('password' , '')


        	user = authenticate(username=username, password=password)

        	if login_form.is_valid:
            	login(request, user)
            	return HttpResponseRedirect('/home/')
            
        # else:
        # return HttpResponseRedirect('/')


    else:
        login_form = UserLoginForm()


    context_login = { 'login_form' : login_form }

    return TemplateResponse(request, 'login_form.html', context_login)