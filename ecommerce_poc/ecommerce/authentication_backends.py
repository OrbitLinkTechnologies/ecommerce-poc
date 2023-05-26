from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

class GoogleOAuthBackend(ModelBackend):
    def authenticate(self, request, email=None, **kwargs):
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return None
        else:
            return user if self.user_can_authenticate(user) else None
