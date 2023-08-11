from django import forms
from .models import *
from django.forms import TextInput, Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re





class PartiForm(forms.ModelForm):
    class Meta:
        model = Parti
        fields = ['matricula','universidad','nombre','ape_patern','ape_mater','grado','carrera','curp','disciplina','rama','FechaIngre','cicloescolar','sexo','nss']
        labels = {
            'FechaIngre': 'Fecha de Ingreso a la Escuela',  # Cambia el label del campo FechaIngre
            'cicloescolar': 'Periodo',  # Cambia el label del campo cicloescolar
        }
        widgets = {
            'matricula': TextInput(attrs={
                'class': "form-control" "small-group",
                'placeholder': 'Matricula',
                'oninput': "this.value = this.value.toUpperCase()"
                }),
            'universidad': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Universidad',
                'oninput': "this.value = this.value.toUpperCase()"
                }),
            'nombre':TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nombre',
                'oninput': "this.value = this.value.toUpperCase()"
                }),
             'ape_patern': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido paterno',
                'oninput': "this.value = this.value.toUpperCase()"
            }),
            'ape_mater': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido materno',
                'oninput': "this.value = this.value.toUpperCase()"
            }),
            'grado':Select(attrs={
                'class': "form-control",
                'placeholder': 'Grado',
                }),
            'carrera':TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Carrera',
                'oninput': "this.value = this.value.toUpperCase()"
                }),
            'curp':TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Curp'
                }),
            'disciplina': Select(attrs={
                'class': "form-control" "small-group",
                'style': 'padding: 10px 16px;'
                'width: 100%;'
                'outline: 0;'
                'margin-bottom: 20px;'
                'border-radius: 20px;'
                'border: 0;'
                'background-color: #ededed;'
                'font-size: 14px;'
                '-webkit-appearance: none;'
                '-moz-appearance: none;'
                'appearance: none;'}),
            'rama': Select(attrs={
                'class': "form-control" "small-group",
                'style': 'padding: 10px 16px;'
                'width: 100%;'
                'outline: 0;'
                'margin-bottom: 20px;'
                'border-radius: 20px;'
                'border: 0;'
                'background-color: #ededed;'
                'font-size: 14px;'
                '-webkit-appearance: none;'
                '-moz-appearance: none;'
                'appearance: none;'}),

             'FechaIngre':  forms.DateInput(attrs={
                'type': 'date', 
                'class': 'form-control',
                'name': 'fecha_ingreso_escuela'
            }),
            'cicloescolar':TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Periodo'
            }),
            'sexo':Select(attrs={
                'class': "form-control",
                'placeholder': 'Sexo'
                }),
            'nss':TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Num. Seguro Social'
                })
        }

class EnterForm(forms.ModelForm):
    fotografia = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = Entre
        fields = ['nombre', 'ape_patern', 'ape_mater', 'telefono_ofic', 'celular', 'disciplina','rama', 'fotografia']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
                'oninput': "this.value = this.value.toUpperCase()"
            }),
            'ape_patern': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido paterno',
                'oninput': "this.value = this.value.toUpperCase()"
            }),
            'ape_mater': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido materno',
                'oninput': "this.value = this.value.toUpperCase()"
            }),
            'telefono_ofic': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de teléfono de oficina',
            }),
            'celular': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de teléfono móvil',
            }),
        }

    def clean_fotografia(self):
        fotografia = self.cleaned_data.get('fotografia')
        # Puedes realizar validaciones adicionales aquí si es necesario
        return fotografia

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.fotografia = self.cleaned_data['fotografia']
        if commit:
            instance.save()
        return instance
        
class ImportForm(forms.Form):
    archivo_excel = forms.FileField()

class UniForm(forms.ModelForm):
    class Meta:
        model = Uni
        fields = '__all__'

class CoordiForm(forms.ModelForm):
    class Meta:
        model = Coordi
        fields = ['Nombre', 'Ape_Pate', 'Ape_Mate', 'telefono_ofic', 'celular', 'email', 'nom_suple', 'cel_suple', 'fotografia']
        widgets = {
            'Nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
                'oninput': "this.value = this.value.toUpperCase()"
            }),
            'Ape_Pate': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido paterno',
                'oninput': "this.value = this.value.toUpperCase()"
            }),
            'Ape_Mate': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido materno',
                'oninput': "this.value = this.value.toUpperCase()"
            }),
            'telefono_ofic': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de teléfono de oficina',
            }),
            'celular': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de teléfono móvil',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico',
            }),
            'nom_suple': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del suplente',
                'oninput': "this.value = this.value.toUpperCase()"
            }),
            'cel_suple': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de teléfono móvil del suplente',
            }),
        }
    

    def clean_fotografia(self):
        fotografia = self.cleaned_data.get('fotografia')
        # Puedes realizar validaciones adicionales aquí si es necesario
        return fotografia

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Puedes realizar validaciones adicionales aquí si es necesario
        return email

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.fotografia = self.cleaned_data['fotografia']
        if commit:
            instance.save()
        return instance


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class AsisForm(forms.ModelForm):
    class Meta:
        model = Asis
        fields = ['nombre', 'ape_patern', 'ape_mater', 'disciplina', 'fotografia']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
                'oninput': "this.value = this.value.toUpperCase()"
            }),
            'ape_patern': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido paterno',
                'oninput': "this.value = this.value.toUpperCase()"
            }),
            'ape_mater': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido materno',
                'oninput': "this.value = this.value.toUpperCase()"
            }),
        }
    def clean_fotografia(self):
        fotografia = self.cleaned_data.get('fotografia')
        # Puedes realizar validaciones adicionales aquí si es necesario
        return fotografia

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.fotografia = self.cleaned_data['fotografia']
        if commit:
            instance.save()
        return instance
    
class MedicForm(forms.ModelForm):
    class Meta:
        model = Medi
        fields = ['nombre', 'ape_patern', 'ape_mater','cedula','email','celular', 'fotografia']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
            }),
            'ape_patern': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido paterno',
            }),
            'ape_mater': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido materno',
            }),
            'cedula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'cedula Profesional',
            }),
             'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico',
            }),
            'celular': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de teléfono móvil',
            }),
            }
    def clean_fotografia(self):
        fotografia = self.cleaned_data.get('fotografia')
        # Puedes realizar validaciones adicionales aquí si es necesario
        return fotografia

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.fotografia = self.cleaned_data['fotografia']
        if commit:
            instance.save()
        return instance
    
class StaffForm(forms.ModelForm):
     class Meta:
        model = Staff
        fields = ['nombre', 'ape_patern', 'ape_mater', 'celular', 'fotografia']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
            }),
            'ape_patern': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido paterno',
            }),
            'ape_mater': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido materno',
            }),
            'celular': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de teléfono móvil',
            }),
            }
     def clean_fotografia(self):
        fotografia = self.cleaned_data.get('fotografia')
        # Puedes realizar validaciones adicionales aquí si es necesario
        return fotografia

     def save(self, commit=True):
        instance = super().save(commit=False)
        instance.fotografia = self.cleaned_data['fotografia']
        if commit:
            instance.save()
        return instance

