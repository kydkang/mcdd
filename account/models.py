from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


## To block a duplicate email address using Django Admin, the following two lines are necessary. 
## https://stackoverflow.com/questions/53461410/make-user-email-unique-django
## Duplicate email address using 'SignUp(Register)' menu is blocked in class UserRegistrationForm.   
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True


## To extend the User model -- based on Django 4 by Example -- Chapter 4 
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)  ## optional field 
    photo = models.ImageField(_('photo'), upload_to='users/%Y/%m/%d', blank=True)  #optional field

    def __str__(self):
        return f'Profile of {self.user.username}' 
    
