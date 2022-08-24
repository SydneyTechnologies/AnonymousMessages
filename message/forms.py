from django import forms
from django.forms import ModelForm
from .models import Message


class UserForm(forms.Form):
    name = forms.CharField(max_length=200)
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'field'
        

class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'field'
        self.fields['password'].widget.attrs['class'] = 'field'

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = "__all__"