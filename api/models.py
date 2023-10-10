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
prodcut_universidad = [
("","--Selecciona una universidad"),
("Universidad Tecnológica de Aguascalientes","Universidad Tecnológica de Aguascalientes"),
("Universidad Tecnológica de Calvillo","Universidad Tecnológica de Calvillo"),
("Universidad Tecnológica del Norte de Aguascalientes","Universidad Tecnológica del Norte de Aguascalientes"),
("Universidad Tecnológica el Retoño","Universidad Tecnológica el Retoño"),
("Universidad Tecnológica Metropolitana de Aguascalientes","Universidad Tecnológica Metropolitana de Aguascalientes"),
("Universidad Tecnológica de Tijuana","Universidad Tecnológica de Tijuana"),
("Universidad Tecnológica de La Paz","Universidad Tecnológica de La Paz"),
("Universidad Tecnológica de Calakmul","Universidad Tecnológica de Calakmul"),
("Universidad Tecnológica de Campeche","Universidad Tecnológica de Campeche"),
("Universidad Tecnológica de Candelaria","Universidad Tecnológica de Candelaria"),
("Universidad Tecnológica de la Selva","Universidad Tecnológica de la Selva"),
("Universidad Tecnológica de Camargo","Universidad Tecnológica de Camargo"),
("Universidad Tecnológica de Chihuahua Sur","Universidad Tecnológica de Chihuahua Sur"),
("Universidad Tecnológica de Ciudad Juárez","Universidad Tecnológica de Ciudad Juárez"),
("Universidad Tecnológica de la Babícora","Universidad Tecnológica de la Babícora"),
("Universidad Tecnológica de la Tarahumara","Universidad Tecnológica de la Tarahumara"),
("Universidad Tecnológica de Paquimé","Universidad Tecnológica de Paquimé"),
("Universidad Tecnológica de Parral","Universidad Tecnológica de Parral"),
("Universidad Tecnológica Paso del Norte","Universidad Tecnológica Paso del Norte"),
("Universidad Tecnológica de Ciudad Acuña","Universidad Tecnológica de Ciudad Acuña"),
("Universidad Tecnológica de Coahuila","Universidad Tecnológica de Coahuila"),
("Universidad Tecnológica de la Región Carbonífera","Universidad Tecnológica de la Región Carbonífera"),
("Universidad Tecnológica de la Región Centro de Coahuila","Universidad Tecnológica de la Región Centro de Coahuila"),
("Universidad Tecnológica de Parras de la Fuente","Universidad Tecnológica de Parras de la Fuente"),
("Universidad Tecnológica de Saltillo","Universidad Tecnológica de Saltillo"),
("Universidad Tecnológica de Torreón","Universidad Tecnológica de Torreón"),
("Universidad Tecnológica del Norte de Coahuila","Universidad Tecnológica del Norte de Coahuila"),
("Universidad Tecnológica de Manzanillo","Universidad Tecnológica de Manzanillo"),
("Universidad Tecnológica de Durango","Universidad Tecnológica de Durango"),
("Universidad Tecnológica de la Laguna Durango","Universidad Tecnológica de la Laguna Durango"),
("Universidad Tecnológica de Poanas","Universidad Tecnológica de Poanas"),
("Universidad Tecnológica de Rodeo","Universidad Tecnológica de Rodeo"),
("Universidad Tecnológica de Tamazula","Universidad Tecnológica de Tamazula"),
("Universidad Tecnológica del Mezquital","Universidad Tecnológica del Mezquital"),
("Universidad Tecnológica de Nezahualcóyotl","Universidad Tecnológica de Nezahualcóyotl"),
("Universidad Tecnológica de Tecámac","Universidad Tecnológica de Tecámac"),
("Universidad Tecnológica de Zinacantepec","Universidad Tecnológica de Zinacantepec"),
("Universidad Tecnológica del Sur del Estado de México","Universidad Tecnológica del Sur del Estado de México"),
("Universidad Tecnológica del Valle de Toluca","Universidad Tecnológica del Valle de Toluca"),
("Universidad Tecnológica Fidel Velázquez","Universidad Tecnológica Fidel Velázquez"),
("Universidad Tecnológica de León","Universidad Tecnológica de León"),
("Universidad Tecnológica de Salamanca","Universidad Tecnológica de Salamanca"),
("Universidad Tecnológica de San Miguel de Allende","Universidad Tecnológica de San Miguel de Allende"),
("Universidad Tecnológica del Norte de Guanajuato (UTNG)","Universidad Tecnológica del Norte de Guanajuato (UTNG)"),
("Universidad Tecnológica del Suroeste de Guanajuato","Universidad Tecnológica del Suroeste de Guanajuato"),
("Universidad Tecnológica Laja Bajío","Universidad Tecnológica Laja Bajío"),
("Universidad Tecnologica de Acapulco","Universidad Tecnologica de Acapulco"),
("Universidad Tecnológica de la Costa Grande de Guerrero","Universidad Tecnológica de la Costa Grande de Guerrero"),
("Universidad Tecnológica de la Región Norte de Guerrero","Universidad Tecnológica de la Región Norte de Guerrero"),
("Universidad Tecnologica de la Tierra caliente","Universidad Tecnologica de la Tierra caliente"),
("Universidad Tecnológica del Mar","Universidad Tecnológica del Mar"),
("Universidad Tecnológica de la Huasteca Hidalguense","Universidad Tecnológica de la Huasteca Hidalguense"),
("Universidad Tecnológica de la Sierra Hidalguense","Universidad Tecnológica de la Sierra Hidalguense"),
("Universidad Tecnológica de la Zona Metropolitana del Valle de México","Universidad Tecnológica de la Zona Metropolitana del Valle de México"),
("Universidad Tecnológica de Mineral de la Reforma","Universidad Tecnológica de Mineral de la Reforma"),
("Universidad Tecnológica de Tulancingo","Universidad Tecnológica de Tulancingo"),
("Universidad Tecnológica de Tula-Tepeji","Universidad Tecnológica de Tula-Tepeji"),
("Universidad Tecnológica del Valle del Mezquital","Universidad Tecnológica del Valle del Mezquital"),
("Universidad Tecnológica Minera de Zimapán","Universidad Tecnológica Minera de Zimapán"),
("Universidad Tecnológica de Jalisco","Universidad Tecnológica de Jalisco"),
("Universidad Tecnológica de la Zona Metropolitana de Guadalajara", "Universidad Tecnológica de la Zona Metropolitana de Guadalajara"),
("Universidad Tecnológica de León", "Universidad Tecnológica de León"),
("Universidad Tecnológica de Morelia","Universidad Tecnológica de Morelia"),
("Universidad Tecnológica del Oriente de Michoacán","Universidad Tecnológica del Oriente de Michoacán"),
("Universidad Tecnológica del Sur del Estado de Morelos","Universidad Tecnológica del Sur del Estado de Morelos"),
("Universidad Tecnológica Emiliano Zapata del Estado de Morelos","Universidad Tecnológica Emiliano Zapata del Estado de Morelos"),
("Universidad Tecnológica de Bahía de Banderas","Universidad Tecnológica de Bahía de Banderas"),
("Universidad Tecnológica de la Sierra","Universidad Tecnológica de la Sierra"),
("Universidad Tecnológica de Mazatan","Universidad Tecnológica de Mazatan"),
("Universidad Tecnológica de Nayarit","Universidad Tecnológica de Nayarit"),
("Universidad Tecnológica de la Costa","Universidad Tecnológica de la Costa"),
("Universidad Tecnológica Bilingüe Franco Mexicana de Nuevo León","Universidad Tecnológica Bilingüe Franco Mexicana de Nuevo León"),
("Universidad Tecnológica Cadereyta","Universidad Tecnológica Cadereyta"),
("Universidad Tecnológica Gral. Mariano Escobedo","Universidad Tecnológica Gral. Mariano Escobedo"),
("Universidad Tecnológica Linares","Universidad Tecnológica Linares"),
("Universidad Tecnológica Santa Catarina","Universidad Tecnológica Santa Catarina"),
("Universidad Tecnológica de la Sierra Sur de Oaxaca","Universidad Tecnológica de la Sierra Sur de Oaxaca"),
("Universidad Técnica de los Valles Centrales Oaxaca","Universidad Técnica de los Valles Centrales Oaxaca"),
("Universidad Tecnológica Bilingüe Internacional y Sustentable de Puebla","Universidad Tecnológica Bilingüe Internacional y Sustentable de Puebla"),
("Universidad Tecnológica de Huejotzingo","Universidad Tecnológica de Huejotzingo"),
("Universidad Tecnológica de Izúcar de Matamoros","Universidad Tecnológica de Izúcar de Matamoros"),
("Universidad Tecnológica de Oriental","Universidad Tecnológica de Oriental"),
("Universidad Tecnológica de Puebla","Universidad Tecnológica de Puebla"),
("Universidad Tecnológica de Tecamachalco","Universidad Tecnológica de Tecamachalco"),
("Universidad Tecnológica de Xicotepec de Juárez","Universidad Tecnológica de Xicotepec de Juárez"),
("Universidad Tecnológica de Tehuacán","Universidad Tecnológica de Tehuacán"),
("Universidad Tecnológica de Corregidora","Universidad Tecnológica de Corregidora"),
("Universidad Tecnologica de Querétaro","Universidad Tecnologica de Querétaro"),
("Universidad Tecnológica de San Juan del Río","Universidad Tecnológica de San Juan del Río"),
("Universidad Tecnológica de Cancún","Universidad Tecnológica de Cancún"),
("Universidad Tecnológica de Chetumal","Universidad Tecnológica de Chetumal"),
("Universidad Tecnológica de la Riviera Maya","Universidad Tecnológica de la Riviera Maya"),
("Universidad Tecnológica Metropolitana de San Luis Potosí","Universidad Tecnológica Metropolitana de San Luis Potosí"),
("Universidad Tecnológica de Culiacán","Universidad Tecnológica de Culiacán"),
("Universidad Tecnológica de Escuinapa","Universidad Tecnológica de Escuinapa"),
("Universidad Tecnológica de Etchojoa","Universidad Tecnológica de Etchojoa"),
("Universidad Tecnológica de Guaymas","Universidad Tecnológica de Guaymas"),
("Universidad Tecnológica de Hermosillo, Sonora","Universidad Tecnológica de Hermosillo, Sonora"),
("Universidad Tecnológica de Nogales","Universidad Tecnológica de Nogales"),
("Universidad Tecnológica de Puerto Peñasco","Universidad Tecnológica de Puerto Peñasco"),
("Universidad Tecnológica de San Luis Río Colorado (BIS)","Universidad Tecnológica de San Luis Río Colorado (BIS)"),
("Universidad Tecnológica del Sur de Sonora","Universidad Tecnológica del Sur de Sonora"),
("Universidad Tecnológica de Tabasco","Universidad Tecnológica de Tabasco"),
("Universidad Tecnológica del Usumacinta","Universidad Tecnológica del Usumacinta"),
("Universidad Tecnológica de Matamoros","Universidad Tecnológica de Matamoros"),
("Universidad Tecnológica de Nuevo Laredo","Universidad Tecnológica de Nuevo Laredo"),
("Universidad Tecnológica de Tamaulipas Norte","Universidad Tecnológica de Tamaulipas Norte"),
("Universidad Tecnológica del Mar de Tamaulipas Bicentenario","Universidad Tecnológica del Mar de Tamaulipas Bicentenario"),
("Universidad Tegnologica de Altamira","Universidad Tegnologica de Altamira"),
("Universidad Tecnológica de Tlaxcala","Universidad Tecnológica de Tlaxcala"),
("Universidad Tecnológica de Gutiérrez Zamora","Universidad Tecnológica de Gutiérrez Zamora"),
("Universidad Tecnológica del Centro de Veracruz","Universidad Tecnológica del Centro de Veracruz"),
("Universidad Tecnológica del Sureste de Veracruz","Universidad Tecnológica del Sureste de Veracruz"),
("Universidad Tecnologica del Centro","Universidad Tecnologica del Centro"),
("Universidad Tecnológica del Mayab","Universidad Tecnológica del Mayab"),
("Universidad Tecnológica del Poniente","Universidad Tecnológica del Poniente"),
("Universidad Tecnológica Metropolitana","Universidad Tecnológica Metropolitana"),
("Universidad Tecnológica Regional del Sur","Universidad Tecnológica Regional del Sur"),
("Universidad Tecnológica del Estado de Zacatecas","Universidad Tecnológica del Estado de Zacatecas"),
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
    universidad = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_universidad
    )

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
    universidad = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_universidad
    )
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
    universidad = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_universidad
    )
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
    universidad = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_universidad
    )
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
    universidad = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_universidad
    )
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
    universidad = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_universidad
    )
    disciplina = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_disciplina
    )
    fotografia = models.ImageField(upload_to="asistentes/")


class Medi(models.Model):
    MedId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    ape_patern = models.CharField(max_length=150)
    ape_mater = models.CharField(max_length=150)
    universidad = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_universidad
    )
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
    universidad = models.CharField(
        max_length=150, default="", null=True, blank=True, choices=prodcut_universidad
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
    fotografia = models.ImageField(upload_to="staff/")
