
from tkinter import Widget
from django import forms
from home.models import Usuario, Categoria






class  UsuarioForm(forms.ModelForm):
    class Meta:     
        model = Usuario
        fields = ['run','nombres','apellidos','fecha_nacimiento','contrasenna','correo_electronico'] #Crea en HTML inputs y etiquetas de dichos campos 
            
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
            