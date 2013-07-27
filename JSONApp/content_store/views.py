from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from .forms import ContentForm

@login_required()
def content_form(request):

    if request.method == 'POST':
        icrs_form = ContentForm(request.POST)

        if icrs_form.is_valid():
            introduction = icrs_form.cleaned_data['introduction']
            concept = icrs_form.cleaned_data['concept']
            reinforcement = icrs_form.cleaned_data['reinforcement']
            summary = icrs_form.cleaned_data['summary']
            icrs_form.save()

            return HttpResponseRedirect('/') # TODO. Currently takes you back to home page, prefer to have 'successful' page

    else:
        icrs_form = ContentForm() # TODO. For the time being, just placing an unbound form here.

    return render(request, 'submit_content.html', {
        'icrs_form': icrs_form, # icrs: intro, concept, reinforcement, summary. ex_form (examples) to follow.
        }) # TODO urls.py needs to be updated for any of these to render