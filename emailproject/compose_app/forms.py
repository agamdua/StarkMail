from django import forms
from django.core.mail import send_mail

class ComposeMessage(forms.Form):
    to = forms.CharField()
    # cc = forms.CharField()
    # bcc = forms.CharField()
    subject = forms.CharField()
    mail_content = forms.TextField()

    if form.is_valid():
        subject = form.cleaned_data['subject']
        mail_content = form.cleaned_data['mail_content']
        recipients.append(to)
        # recipients.append(cc)
        # recipients.append(bcc)
        sender = agam@tutorific.co # Hard coding user email

        send_mail(subject, mail_content, sender, recipients)
        return HttpResponseRedirect('/thanks/') # Redirect after post


