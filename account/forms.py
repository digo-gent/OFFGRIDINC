from django.forms.models import ModelForm
from django.contrib.auth import authenticate
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import Account

class AccountCreationForm(UserCreationForm):
    
        password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
        password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)
        
        class Meta:
            model = Account
            fields = ("email","username")
            
        def clean_password2(self):
            # Check that the two password entries match
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            
            if password1 and password2 and password1 != password2:
                raise ValidationError("Passwords don't match")
            return password2

        def save(self, commit=True):
            # Save the provided password in hashed format
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            
            if commit:
                user.save()
            return user
        
class AccountChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ["email", "password", "username", "is_active", "is_admin"]
        
    def form_valid(self, form):
        messages.success(self.request, "Your account has been updated successfully.")
        return super().form_valid(form)
        
#Authenticate
class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")

