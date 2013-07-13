from .models import InboxModels
from django.shortcuts import render

# Create your views here.

def on_incoming_emails(request):
	if request.method == 'POST':
		sender = request.POST.get('sender')
		recipient = request.POST.get('recipient')
		subject = request.POST.get('subject', '')
		body_plain = request.POST.get('body-plain', '')

		final_incoming_mail = InboxModels(sender=sender, recipient=recipient, subject=subject, mail_text=body_plain)

		final_incoming_mail.save()

	return HttpResponse('OK')

def inbox_view(request):
	return render(request, 'inbox.html', {'mail': InboxModels.objects.all()})