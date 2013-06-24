# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def compose(request):
    if request.method == 'POST':
        form = ComposeMessage(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            mail_content = form.cleaned_data['mail_content']
            recipients.append(to)
            # recipients.append(cc)
            # recipients.append(bcc)
            sender = agamdua@gmail.com # Hard coding user email
                
            send_mail(subject, mail_content, sender, recipients)
            return HttpResponseRedirect('/thanks/') # Redirect after post

    else:
        form = ComposeMessage() # An unbound form
        
    return render(request, 'compose.html', {
        'form': form,
        })

