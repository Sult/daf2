from django.db import models
from django.contrib.auth.models import User



class UserControl(models.Model):
    """ see if a user has been accepted """
    
    user = models.OneToOneField(User)
    confirmed = models.BooleanField(default=False)
