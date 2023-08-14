from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput())
    password = forms.CharField(widget= forms.PasswordInput())

    class meta:
        model = User
        fields = ['username', 'password']

class PerfilForm(UserCreationForm):
    username = forms.CharField(widget= forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese el nombre de usuario'}
    ))
    password1 = forms.CharField(widget= forms.PasswordInput(
        attrs= {'class': 'form-control', 'placeholder': 'Ingrese la contraseña'}
    ))
    password2 = forms.CharField(widget= forms.PasswordInput(
        attrs= {'class': 'form-control', 'placeholder': 'Confirme la contraseña'}
    ))

    telefono = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingrese el telefono'}
    ))
    direccion = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingrese la direccion'}
    ))
    cedula = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingrese la cedula'}
    ))
    foto = forms.ImageField()


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre', 'direccion', 'correo', 'telefono', 'fk_usuario']
        labels = {
            'nombre' : 'Nombre',
            'direccion' : 'Direccion',
            'correo' : 'Correo',
            'telefono' : 'Telefono',
            'fk_usuario' : 'Usuario',
        }
        widgets  = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'id': "nombre"

                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un direccion',
                    'id': "direccion"

                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un correo',
                    'id': "correo"

                }
            ),
            'telefono': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un telefono',
                    'id': "telefono"

                }
            ),
            'fk_usuario': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un usuario',
                    'id': "fk_usuario"

                }
            ),
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['user', 'name', 'lastname', 'email']
        labels = {
            'user':'Usuario',
            'name' : 'Nombre',
            'lastname': 'Apellido',
            'email': 'Correo',

        }
        widgets = {
            'user': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Usuario',
                    'id': "usuario"
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'id': "nombre"
                }
            ),
            'lastname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un apellido',
                    'id': "apellido"
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un correo',
                    'id': "correo"
                }
            ),
        }

class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ['origen', 'destino', 'fecha_hora', 'precio', 'clase', 'cupo', 'fk_ruta', 'fk_bus']
        labels = {
            'origen': 'Origen',
            'destino': 'Destino',
            'fecha_hora': 'Fecha',
            'precio': 'Precio',
            'clase': 'Clase',
            'cupo': 'Cupo',
            'fk_ruta': 'Ruta',
            'fk_bus': 'Bus',
        }
        widgets = {
            'origen': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el Origen',
                    'id': "origen"

                }
            ),
            'destino': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el destino',
                    'id': "destino"

                }
            ),
            'fecha_hora': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la fecha: dd/mm/aa hh',
                    'id': "fecha"

                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el precio',
                    'id': "precio"

                }
            ),
            'clase': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la clase',
                    'id': "clase"

                }
            ),
            'cupo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el cupo',
                    'id': "cupo"

                }
            ),
            'fk_ruta': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione la ruta',
                    'id': "ruta"

                }
            ),
            'fk_bus': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione el bus',
                    'id': "bus"

                }
            ),

        }
        

