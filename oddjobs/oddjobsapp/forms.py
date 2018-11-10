from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, help_text='First Name')
    last_name = forms.CharField(max_length=30, help_text='Last Name')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField()
