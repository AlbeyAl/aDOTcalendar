from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from index.models import a_dot_user

class User(ModelBackend):
    """
    Customer user auth backend.
    """
    
    def authenticate(self, request, **kwargs):
        user_id = kwargs['username']
        user_password = kwargs['password']
        user_auth = None

        try:
            user_auth = a_dot_user.objects.get(user_id=user_id)

            if user_auth.user_auth.check_password(user_password) is True:
                return user_auth
        except a_dot_user.DoesNotExist:
            pass
