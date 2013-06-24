from django.db import models

# Create your models here.

class ComposeModel(models.Model):
    to = models.TextField()
    # cc
    # bcc
    subject = models.CharField(max_length=100)
    mail_content = models.TextField()
