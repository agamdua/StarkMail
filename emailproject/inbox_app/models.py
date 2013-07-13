from django.db import models

# Create your models here.

class InboxModels(models.Model):
	sender = models.EmailField()
	recipient = models.TextField()
	subject = models.CharField(max_length=100)
	mail_text = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)