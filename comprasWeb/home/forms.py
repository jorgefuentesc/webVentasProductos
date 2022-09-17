
from django import forms
from home.models import Usuario



class  UsuarioForm(forms.ModelForm):
    class Meta:     
        model = Usuario
        fields = ['run','nombres','apellidos','fecha_nacimiento','usuario','contrasenna','correo_electronico','telefono','ciudad','comuna','direccion'] #Crea en HTML inputs y etiquetas de dichos campos 
            
