from django import forms
from . import messages, validators
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from allauth.account.models import EmailAddress
from .models import User
from allauth.account.utils import send_email_confirmation
from .utils import send_email_update_notification
from phonenumbers import parse as parse_phone
from phonenumbers import NumberParseException


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
        phone = self.data.get('phone')
        username = self.data.get('username')

        if len(username) and username.casefold() in password.casefold():
            errors.append("Password is too similar to the username.")

        email = email.split('@')
        if email[0].casefold() in password.casefold():
            errors.append("Password cannot contain your email.")

        if phone and validators.phone_validator(phone):
            try:
                phone = str(parse_phone(phone).national_number)
                if phone in password:
                    errors.append("Passwords cannot contain your phone.")
            except NumberParseException:
                pass

        if errors:
            raise forms.ValidationError(errors)
        return password

    def clean_email(self):
        email = self.data.get('email')
        email = email.casefold()
        if EmailAddress.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "User with this email address already exists.")

        return email

    def clean_phone(self):
        phone = self.data.get('phone')
        if phone:
            if User.objects.filter(phone=phone).exists():
                raise forms.ValidationError(
                    "User with this Phone number already exists.")
            try:
                parse_phone(phone)
            except NumberParseException:
                raise forms.ValidationError(
                    "Please enter a valid country code.")
        else:
            phone = None
        return phone

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class UserSettingsForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    phone = forms.RegexField(regex=r'^\+[0-9]{5,14}$',
                             error_messages={'invalid': messages.phone_format},
                             required=False)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'full_name']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.current_email = self.instance.email
        self.current_phone = self.instance.phone
        self.current_username = self.instance.username

    def clean_username(self):
        username = self.data.get('username')
        if username.casefold() != self.current_username.casefold():
            validators.check_username_case_insensitive(username)

        if username.lower() in settings.ACCOUNT_USERNAME_BLACKLIST:
            raise forms.ValidationError("Kindly use a different username.")

        return username

    def clean_email(self):
        email = self.data.get('email')
        email = email.casefold()
        if(email != self.current_email and
           EmailAddress.objects.filter(email=email).exists()):
            raise forms.ValidationError(
                "User with this email address already exists.")

        return email

    def clean_phone(self):
        phone = self.data.get('phone')
        if phone:
            if (phone != self.current_phone and
                    User.objects.filter(phone=phone).exists()):
                raise forms.ValidationError(
                    ("User with this Phone number already exists."))
            try:
                parse_phone(phone)
            except NumberParseException:
                raise forms.ValidationError(
                    ("Please enter a valid country code."))
        else:
            phone = None

        return phone

    def clean_password(self):
        if (not self.instance.check_password(self.data.get('password'))):
            raise forms.ValidationError(
                "Please provide the correct password for your account.")

    def save(self, *args, **kwargs):
        user = super().save(commit=False, *args, **kwargs)
        if user.email != self.current_email:
            self.instance.emailaddress_set.all().delete()
            send_email_confirmation(self.request, user)
            send_email_update_notification(self.current_email)
            user.email = self.current_email
        user.save()
        return user
