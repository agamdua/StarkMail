from django import forms

class ComposeMessage(forms.Form):
    to = forms.CharField()
    # cc = forms.CharField()
    # bcc = forms.CharField()
    subject = forms.CharField()
    mail_content = forms.TextField()
