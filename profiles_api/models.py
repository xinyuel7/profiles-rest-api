from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models and inherit from the abstract base user classes
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email: #if email ="" or null
            raise ValueError('User must have an email address') #ensure that a proper email address has been passed if __name__ == '__main__':
        #standardize the second half of email address(case insensitive)
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)   #create a new users
        user.set_password(password) #set_password function ensures that password is encrypted(converted into a hash and never stored as plain text in the database)
        user.save(using=self._db) #can support multiple databases

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password) #self is automaticaaly passed in when you call any class functions
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile( AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)  #email column on our user profile database table
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) #if the user has access to the django admin

#specify the model manager so that we can create and control users using the command line
    objects = UserProfileManager()

    USERNAME_FIELD = 'email' #authenticate users instead of providing a user name and password, they provide email and password
    REQUIRED_FIELDS =['name']

    def get_full_name(self): #define function in a class, must specify self as the first argument
        """Retrieve full name of user"""
        return self.name
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    def __str__(self):  #string representation of a model (convert a user profile object into a string) recommended!
        """string representation of our user"""
        return self.email
