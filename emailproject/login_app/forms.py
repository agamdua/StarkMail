from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password,
                                           request=self.request)
            if self.user_cache is None:
                raise forms.ValidationError(
                    _('Please enter a correct username and password. '
                      'Note that both fields are case-sensitive.'),
                )
            elif not self.user_cache.is_active:
                raise forms.ValidationError(_('This account is inactive.'))
        self.check_for_test_cookie()
        return self.cleaned_data
