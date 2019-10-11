from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self,email, password=None, **extra_fields):
        """Creates and saves new user"""
        if not email:
            raise ValueError("no email provided")
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email, password=None, **extra_fields):
        """Creates and saves new user"""
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    """Custom User Model supports email instead of username"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'


class Room(models.Model):
    """Room object to be used """
    total_seat = models.IntegerField()
    def __str__(self):
        return str(self.id)

class Movie(models.Model):
    """Movie object to be used """
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    showtime = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)
        
class Tickets(models.Model):
    """Room object to be used """
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    ticket_available = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.id)

class Order(models.Model):
    """Room object to be used """
    tickets_id = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)