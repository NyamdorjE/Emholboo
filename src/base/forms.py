from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _



class EmployeeForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'username_already_exist': _("Username already exist."),
    }
    username = forms.CharField(label=_('Username'))
    email = forms.CharField(
        label=_('Email'),
        widget=forms.EmailInput()
    )
    last_name = forms.CharField(label=_('Last name'))
    first_name = forms.CharField(label=_('First name'))
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        label=_('Confirm password'),
        widget=forms.PasswordInput()
    )

    class Meta:
        model = Employee
        fields = []

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                self.error_messages['username_already_exist'],
                code='username_already_exist',
            )
        return username

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return confirm_password
