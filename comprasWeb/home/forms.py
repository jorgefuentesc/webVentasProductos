
from tkinter import Widget
from django import forms
from home.models import  Categoria
from users.models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 






class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electronico'
        }
# class  UsuarioForm(forms.ModelForm):
#     class Meta:     
#         model = Usuario
#         fields = ['run','nombres','apellidos','fecha_nacimiento','contrasenna','correo_electronico'] #Crea en HTML inputs y etiquetas de dichos campos 
            
class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['categoria_nombre','categoria_vigencia']
        labels = {
            'categoria_nombre': 'Nombre de la categoria',
            'categoria_vigencia': 'Estado de la categoria a ticket habilidado / blanco des habilidado'
        }
        widgets = {
            'categoria_nombre': forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'categoria_vigencia': forms.CheckboxInput(
                attrs = {
                    'class': 'form-control'
                }
            )
        }
            