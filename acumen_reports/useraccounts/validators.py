from django.core.exceptions import ValidationError

import re
from .models import User


def check_username_case_insensitive(username):
    usernames = [
        u.casefold() for u in
        User.objects.values_list('username', flat=True)
    ]
    if username.casefold() in usernames:
        raise ValidationError(
            ("A user with that username already exists")
        )


def phone_validator(phone):
    pattern = r'^\+(?:[0-9]?){6,14}[0-9]$'
    if re.match(pattern=pattern, string=str(phone)):
        return True
    else:
        return False
