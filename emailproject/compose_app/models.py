from django.db import models

# Create your models here.

class ComposeModel(models.Model):
    to = models.TextField()
    cc = models.TextField()
    bcc = models.TextField()
    subject = models.CharField(max_length=100)
    mail_text = models.TextField()
    # timestamp = models.DateTimeField(auto_now_add=True)



