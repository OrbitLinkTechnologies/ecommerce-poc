from django.contrib.auth.models import User
from ecommerce.models import Customer
import json

def associate_by_email(backend, details, response, user=None, *args, **kwargs):
    """
    Associate current auth with a user with the same email address in the DB.
    Used for platforms that don't provide a user ID.
    """
    if user:
        return None
    
    try:
        user = User.objects.get(email=details['email'])
    except User.DoesNotExist:
        return None
    
    return {'user': user, 'is_new': False}

def check_email_verified(backend, details, response, user=None, *args, **kwargs):
    """
    Check if the email address provided by the social authentication provider is verified.
    """
    if backend.name == 'google-oauth2':
        is_verified = response.get('email_verified', False)
    else:
        is_verified = False
    
    if not is_verified:
        raise ValueError("The email address provided by the social provider is not verified.")
    
    return None

def save_oauth_user_id(backend, user, response, *args, **kwargs):
    print('-------------------------------------------------')
    print('save oauth user to django app')
    print('-------------------------------------------------')
    print(json.dumps(response))
    print('-------------------------------------------------')
    print('save oauth user to django app')
    print('-------------------------------------------------')
    if backend.name == 'google.oauth2':
        oauth_user_id = response.get('id')
        profile, created = Customer.objects.get_or_create(user=user)
        profile.oauth_user_id = oauth_user_id
        profile.save()