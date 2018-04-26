from django import forms
from . import messages
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from allauth.account.models import EmailAddress
from .models import User


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    phone = forms.RegexField(regex=r'^\+[0-9]{5,14}$',
                             error_messages={'invalid': messages.phone_format},
                             required=False)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password', 'full_name']

    def clean_username(self):
        username = self.data.get('username')
        if username.lower() in settings.ACCOUNT_USERNAME_BLACKLIST:
            raise forms.ValidationError("Kindly use a different username.")

        return username

    def clean_password(self):
        password = self.data.get('password')
        validate_password(password)
        errors = []

        email = self.data.get('email')
        # phone= self.data.get('phone')
        username = self.data.get('username')

        if len(username) and username.casefold() in password.casefold():
            errors.append("Password is too similar to the username.")
        if email:
            email = email.split('@')
            if email[0].casefold() in password.casefold():
                errors.append("Password cannot contain your email.")
        if errors:
            raise forms.ValidationError(errors)
        return password

    def clean_email(self):
        email = self.data.get('email')
        if email:
            email = email.casefold()
            if EmailAddress.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "User with this email address already exists.")
        else:
            email = None

        return email

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
