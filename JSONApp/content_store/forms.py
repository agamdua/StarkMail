from django.forms import ModelForm
from .models import Content, Examples
from ckeditor.widgets import CKEditorWidget


class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ('introduction', 'concept', 'reinforcement', 'summary')
        # Have not included difficulty level, because did not like the representation in the models. Would prefer use of LEVEL_CHOICES.

        widgets = {
            'introduction': CKEditorWidget(),
            'concept': CKEditorWidget(),
            'reinforcement': CKEditorWidget(),
            'summary': CKEditorWidget(),
            }
