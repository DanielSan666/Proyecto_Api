from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from email_validator import validate_email, EmailNotValidError


prodcut_disciplina = [
    ("", "-- Seleccione una disciplina --"),
    ("Ajedrez", "Ajedrez"),
    ("Atletismo", "Atletismo "),
    ("Baloncesto", "Baloncesto"),
    ("Canto", "Canto"),
    ("Declamacion", "Declamacion"),
    ("Oratoria", "Oratoria"),
    ("Voleibol", "Voleibol"),
    ("Taekwondo", "Taekwondo"),
    ("Mural en gis", "Mural en gis"),
    ("Softbol", "Softbol"),
    ("Rondalla", "Rondalla"),
    ("Fútbol 7", "Fútbol 7"),
    ("Futbol asociacion", "Futbol asociacion"),
]

prodcut_rama = [
    ("", "-- Seleccione una Rama --"),
    ("Varonil", "Varonil"),
    ("Femenil", "Femenil"),
    ("Mixto", "Mixto"),
]

prodcut_sexo = [
    ("", "--Seleccione el sexo--"),
    ("Hombre", "Hombre"),
    ("Mujer", "Mujer"),
]
prodcut_grado = [
    ("", "--Seleccione el Grado--"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
]


class Usuario(models.Model):
    USUARIO = "U"
    ADMINISTRADOR = "A"
    SUPERUSUARIO = "S"

    tipos_usuarios = [
        (USUARIO, "Usuario"),
        (ADMINISTRADOR, "Administador"),
        (SUPERUSUARIO, "Super usuario"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    tipo = models.CharField(max_length=1, default=USUARIO, choices=tipos_usuarios)
    disciplina = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_disciplina
    )
    universidad = models.CharField(max_length=150)

    def __str__(self):
        return str(self.user)


# Participantes
def validate_curp(value):
    # Expresión regular para validar el formato del CURP
    curp_pattern = r"^[A-Z]{4}\d{6}[HM][A-Z]{5}\d{2}$"
    if not re.match(curp_pattern, value):
        raise ValidationError("El CURP ingresado no es válido.")


def validate_nss(value):
    # Expresión regular para validar el formato del NSS (Número de Seguridad Social)
    nss_pattern = r"^\d{11}$"
    if not re.match(nss_pattern, value):
        raise ValidationError("El NSS ingresado no es válido.")


class Parti(models.Model):
    PartiId = models.AutoField(primary_key=True)
    matricula = models.IntegerField()
    universidad = models.CharField(max_length=150)
    nombre = models.CharField(max_length=150)
    ape_patern = models.CharField(max_length=150)
    ape_mater = models.CharField(max_length=150)
    grado = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_grado
    )
    carrera = models.CharField(max_length=150)
    curp = models.CharField(
        max_length=150,
        validators=[
            validate_curp,
        ],
    )
    disciplina = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_disciplina
    )
    rama = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_rama
    )
    FechaIngre = models.DateField()
    cicloescolar = models.CharField(max_length=150)
    sexo = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_sexo
    )
    nss = models.CharField(
        max_length=150,
        validators=[
            validate_nss,
        ],
    )

    def __str__(self):
        return self.nombre


# Entrenadores
class Entre(models.Model):
    EntreId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    ape_patern = models.CharField(max_length=150)
    ape_mater = models.CharField(max_length=150)
    telefono_ofic = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\d{1,10}$",
                message="El número de casa debe tener entre 1 y 10 dígitos.",
            )
        ],
    )
    celular = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,10}$",
                message="El número de teléfono móvil debe tener entre 9 y 10 dígitos.",
            )
        ],
    )

    disciplina = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_disciplina
    )
    rama = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_rama
    )
    fotografia = models.ImageField(upload_to="imagenes/")


# Universidades
class Uni(models.Model):
    uniId = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=150)
    universidad = models.CharField(max_length=150)
    clave = models.BigIntegerField()
    camiones = models.IntegerField()
    vans = models.IntegerField()
    carros = models.IntegerField()
    hotel = models.CharField(max_length=150)
    requerimientos = models.CharField(max_length=150)
    guias = models.IntegerField()
    fotografia = models.ImageField(upload_to="universidad/")
    carta_protes = models.FileField(upload_to="archivos/")


class Coordi(models.Model):
    corId = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=150)
    Ape_Pate = models.CharField(max_length=150)
    Ape_Mate = models.CharField(max_length=150)
    telefono_ofic = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\d{1,10}$",
                message="El número de casa debe tener entre 1 y 10 dígitos.",
            )
        ],
    )
    celular = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,10}$",
                message="El número de teléfono móvil debe tener entre 9 y 10 dígitos.",
            )
        ],
    )
    email = models.EmailField()
    nom_suple = models.CharField(max_length=150)
    cel_suple = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,10}$",
                message="El número de teléfono móvil debe tener entre 9 y 10 dígitos.",
            )
        ],
    )
    fotografia = models.ImageField(upload_to="coordinadores/")


class Asis(models.Model):
    AsId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    ape_patern = models.CharField(max_length=150)
    ape_mater = models.CharField(max_length=150)
    disciplina = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_disciplina
    )
    fotografia = models.ImageField(upload_to="asistentes/")


class Medi(models.Model):
    MedId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    ape_patern = models.CharField(max_length=150)
    ape_mater = models.CharField(max_length=150)
    cedula = models.CharField(max_length=150)
    email = models.EmailField()
    celular = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,10}$",
                message="El número de teléfono móvil debe tener entre 9 y 10 dígitos.",
            )
        ],
    )
    fotografia = models.ImageField(upload_to="medicos/")


class Staff(models.Model):
    StId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    ape_patern = models.CharField(max_length=150)
    ape_mater = models.CharField(max_length=150)
    celular = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,10}$",
                message="El número de teléfono móvil debe tener entre 9 y 10 dígitos.",
            )
        ],
    )
    fotografia = models.ImageField(upload_to="staff/")
