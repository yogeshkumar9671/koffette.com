from cProfile import label
from dataclasses import field
import email
from statistics import mode
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation
from app.models import Customer



class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.TextInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password' ]


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Your Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))



class PasswordChangeForm(PasswordChangeForm):
        # error_css_class = 'has-error'
        # error_messages = {'password_incorrect': "Your password is incorrect"}
        old_password = forms.CharField(label=("Old Password"),strip=False, widget=forms.PasswordInput(attrs={"autocomplete":"current-password", 'autofocus': True, 'class':'form-control'}))
        new_password1 = forms.CharField(label=("New Password"),strip=False, widget=forms.PasswordInput(attrs={"autocomplete":"new-password", 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
        new_password2 = forms.CharField(label=("Confirm New Password"),strip=False, widget=forms.PasswordInput(attrs={"autocomplete":"new-password", 'class':'form-control'}))


class ForgotPasswordForm(PasswordResetForm):
    email = forms.EmailField(label=("Email"), max_length=254, widget=forms.EmailInput(attrs={"autocomplete":"email", "placeholder":"Enter Your Email", "class":"form-control"}))


class SetForgotPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=("New password"), widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', "class":"form-control"}), strip=False, help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=("New password confirmation"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', "class":"form-control"}) )


class CustomerAddressForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'state', 'pincode'] 
        widgets = {
        'name':forms.TextInput(attrs={'class': 'form-control'}),
        'locality':forms.TextInput(attrs={'class': 'form-control'}),
        'city':forms.TextInput(attrs={'class': 'form-control'}),
        'state':forms.Select(attrs={'class': 'form-control'}),
        'pincode':forms.NumberInput(attrs={'class': 'form-control'}),
        }