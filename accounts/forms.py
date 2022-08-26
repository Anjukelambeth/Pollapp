from tkinter import Widget
from django import forms
from django.contrib.auth.models import User


# class UserRegistrationForm(forms.ModelForm):
#     class Meta:
#         model  = User
#         fields = ['username','phone_number','email','password']
#         widgets={
#             'password':forms.PasswordInput()
#         }

#     def save(self, commit =True):
#         user= super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         if commit:
#             user.save()
#         return user

# from tkinter import Widget
from django.forms import ValidationError
from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
 
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter your password',
        'class':'form-control'
    }))
    confirm_password =forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm password',
        'class':'form-control'
    }))
    class Meta:
        model  = Account
        fields = ['first_name','last_name','phone_number','email','password']

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder']= 'Enter your first name'
        self.fields['last_name'].widget.attrs['placeholder']= 'Enter your last name'
        self.fields['email'].widget.attrs['placeholder']= 'Enter your email address'
        self.fields['phone_number'].widget.attrs['placeholder']= 'Enter your phone number'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class']= 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password=cleaned_data.get('password')
        confirm_password =cleaned_data.get('confirm_password')
        if password!= confirm_password:
            raise forms.ValidationError(
                'password and confirm password does not match'
            )
