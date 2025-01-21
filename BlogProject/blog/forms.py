from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import Post
from django.utils.translation import gettext, gettext_lazy as _

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    password2 = forms.CharField(label="Re-enter Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']
        labels = {'email':'Email','first_name':'First Name', 'last_name':'Last Name'}

        widgets ={'username' : forms.TextInput(attrs={'class':'form-control'}),
                  'first_name' : forms.TextInput(attrs={'class':'form-control'}),
                  'last_name' : forms.TextInput(attrs={'class':'form-control'}),
                  'email' : forms.EmailInput(attrs={'class':'form-control'}),
                  
                  }

class LoginForm(AuthenticationForm):
    username = UsernameField(label="Username", widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'autocomplet':'current-password','class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','password']
        labels = {'username':'Username','password':'Password'}
        widgets ={'username' : forms.TextInput(attrs={'class':'form-control'}),
                  'password' : forms.PasswordInput(attrs={'class':'form-control'}),
                  }

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']
        widgets ={'title' : forms.TextInput(attrs={'class':'form-control'}),
                  'content' : forms.Textarea(attrs={'class':'form-control'}),
                  }
