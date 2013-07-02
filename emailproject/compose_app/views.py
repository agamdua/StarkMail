# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from forms import ComposeForm

def compose(request):
    
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
            sender = 'agamdua@gmail.com' # Hard coding user email

            form.save()
                
            send_mail(subject, mail_text, sender, recipients)
            return HttpResponseRedirect('/compose/') # Redirect after post

    else:
        form = ComposeForm() # An unbound form
        
    return render(request, 'compose.html', {
        'form': form,
        })

