# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class Link(models.Model):
    managed = True
    id = models.OneToOneField('Recipe', models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    email = models.ForeignKey('Users', models.DO_NOTHING, db_column='email', to_field=None)

    #class Meta:
    #    managed = False
    #    db_table = 'LINK'


class Recipe(models.Model):
    managed = True
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)

    def ingredients_as_list(self):
        return self.ingredients.split("\n")
    def instructions_as_list(self):
        return self.instructions.split("\n")
    #class Meta:
        #managed = False
        #db_table = 'RECIPE'


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class Users(AbstractUser):
    
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    managed = True
    objects = UserManager()
    #class Meta:
    #    managed = False
    #    db_table = 'USERS'
