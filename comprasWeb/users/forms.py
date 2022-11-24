from . import models
from django import forms

class LoginUsuario(forms.Form):
    email = forms.EmailField(
        widget= forms.TextInput(
            attrs={
                'id': 'loginEmail',
                'type': 'email',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                'id': 'loginPassword',
                'type': 'password',
                'class': 'form-control'
            }
        )
    )


class RegistroUsuario(forms.Form):
    email = forms.EmailField(
        widget = forms.TextInput(
            attrs={
                'id': 'registroEmail',
                'type': 'email',
                'class': 'form-control'
            }
        )
    )
    nombres = forms.CharField(
        max_length=100,
        widget = forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control'
            }
        )
    )

    apellidos = forms.CharField(
        max_length=100,
        widget = forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                'id': 'registroPassword',
                'type': 'password',
                'class': 'form-control'
            }
        )
    )
    password2 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control'
            }
        )
    )
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden ')
        return cd['password2']