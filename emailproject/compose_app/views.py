# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .forms import ComposeForm
# from .send_mail import send_simple_message
from untracked import auth, api_url

import requests


@login_required()
def compose(request):
    username = request.user.username
    recipients = []

    if request.method == 'POST':
        form = ComposeForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            mail_text = form.cleaned_data['mail_text']
            to = form.cleaned_data['to']
            recipients.append(to)
            # recipients.append(cc)
            # recipients.append(bcc)
            sender = username + "@starkmail.mailgun.org"
            form.save()

            # send_mail(subject, mail_text, sender, recipients)
            requests.post(
                url=api_url,
                auth=auth,
                data = {"from" : sender,
                        "to" : recipients,
                        "subject" : subject,
                        "text" : mail_text },
                verify=False)

            return HttpResponseRedirect('/compose/') # Redirect after post

    else:
        form = ComposeForm() # An unbound form
        
    return render(request, 'compose.html', {
        'form': form,
        })

