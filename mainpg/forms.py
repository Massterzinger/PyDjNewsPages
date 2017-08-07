from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for i in self.fields.keys():
            self.fields[i].widget.attrs['class'] = 'w3-input w3-border w3-light-grey'
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

class UserLogInForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(UserLogInForm, self).__init__(*args, **kwargs)
        for i in self.fields.keys():
            self.fields[i].widget.attrs['class'] = 'w3-input w3-border w3-light-grey'
    class Meta:
        model = User
        fields = ['username', 'password']
