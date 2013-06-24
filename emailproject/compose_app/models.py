from django.db import models

# Create your models here.

class ComposeModel(models.Model):
    to = models.CharField()
    # cc
    # bcc
    subject = models.CharField()
    mail_content = forms.TextField()
