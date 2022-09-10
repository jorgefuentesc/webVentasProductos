from django import forms
from home.models import Usuario

class  UsuarioForm(forms.ModelForm):
    class Meta:     
        model = Usuario
        fields = ['run','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','correo_electronico','telefono','direccion','region','ciudad','fecha_nacimiento'] #Crea en HTML inputs y etiquetas de dichos campos 
            
