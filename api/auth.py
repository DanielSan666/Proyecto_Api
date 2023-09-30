from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class AuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            raise ValidationError("Invalid username/password")

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
