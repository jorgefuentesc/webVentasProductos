import random

from email.policy import default
from enum import unique
import string
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class CustomAccountManager(BaseUserManager):
    def create_user( self, email, nombres, apellidos, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an correo_electronico addres'))
        email = self.normalize_email(email)
        user = self.model( email = email, nombres = nombres, apellidos = apellidos, **other_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, nombres, apellidos, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('superUser must be assigned to is_staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('superUser must be assigned to is_superuser=True.')

        return self.create_user(email, nombres, apellidos, password, **other_fields)
        
        
        
 # contrasenna = models.CharField(max_length=220,blank=True,null=True)
class Usuario(AbstractBaseUser,PermissionsMixin):
    usuario_id = models.AutoField(primary_key=True)
    run = models.CharField(max_length=20,blank=True,null=True)
    nombres = models.CharField(max_length=220,blank=True,null=True)
    apellidos = models.CharField(max_length=220,blank=True,null=True)
    # fotografia = models.ImageField
    fecha_nacimiento = models.CharField(max_length=220,blank=True,null=True)
    usuario = models.CharField(max_length=220, blank=True,null=True)
   
    email = models.EmailField(_('email'), unique = True, blank=True,null=True)
    telefono = models.CharField(max_length=20,blank=True, null=True)
    ciudad = models.CharField(max_length=220,blank=True,null=True)
    comuna = models.CharField(max_length=220,blank=True,null=True)
    direccion = models.CharField(max_length=220,blank=True,null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_vigencia = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['nombres','apellidos']

    
    
    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    def get_absolute_url(self):
        return reverse('users:detalle_usuario', args=[self.slug])
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.email)
        super(Usuario, self).save(*args, **kwargs)\
