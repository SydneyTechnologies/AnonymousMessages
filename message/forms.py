from django import forms


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
