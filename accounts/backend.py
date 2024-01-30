from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend


class EmailOrUsernameLogin(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
               user = User.objects.get(username=username)
            except:
                return None
            
        if user.check_password(password):
            return user
        
        return None
    
            
            
    