from django.forms import ModelForm
from .models import ComposeModel

class ComposeForm(ModelForm):
	class Meta:
		model = ComposeModel