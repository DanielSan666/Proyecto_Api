from django.contrib import admin
from django.urls import path, include
from api.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    #Login y logout
   
    path('salir/', salir, name='salir'),
    path('registro/', registro, name='registro'),
    path('usuarios', usuarios, name='usuarios' ),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),


    #Participantes
    path('', inicio, name='home'),
    path('participantes', participantes, name='index'),
    path('crear_parti/', crearParti, name='crear_parti'),
    path('editar_parti/<int:PartiId>/', editarParti, name='editar_parti'),
    path('eliminar_parti/<int:PartiId>/', eliminarParti, name='eliminar_parti'),

    #Entrenadores
    path('entrenadores/', entrenadores, name='entrenadores'),
    path('entrenadores/crear_entre/', crearEntre, name='crear_entre'),
    path('entrenadores/editar_entre/<int:EntreId>',editarEntre, name='editar_entre'),
    path('entrenadores/eliminar_entre/<int:EntreId>',eliminarEntre, name='eliminar_entre'),

    #Universidades
    path('universidades/', universidades, name='universidades'),
    path('universidades/crear_uni/', crearUni, name='crear_uni'),
    path('universidades/editar_uni/<int:uniId>/', editarUni, name='editar_uni'),
    path('universidades/eliminar_uni/<int:uniId>',eliminarUni, name='eliminar_uni'),

    #Coordinadores
    path('coordinadores/', coordinadores, name='coordinadores'),
    path('coordinadores/crear_coordi', crearCoordi, name='crear_coordi'),
    path('coordinadores/editar_coordi/<int:corId>',editarCoordi, name='editar_coordi'),
    path('coordinadores/eliminar_coordi/<int:corId>',eliminarCoordi, name='eliminar_coordi'),


    #Asistentes
    path('asistentes/', asistente, name='asistentes'),
    path('asistentes/crear_asis', crearAsis, name='crear_asis'),
    path('asistentes/editar_asis/<int:AsId>',editarAsis, name='editar_asis'),
    path('asistentes/eliminar_asis/<int:AsId>',eliminarAsis, name='eliminar_asis'),

    #Medicos
    path('medicos/', medicos, name='medicos'),
    path('medicos/crear_medic', crearMedic, name='crear_medic'),
    path('medicos/editar_medic/<int:MedId>',editarMedic, name='editar_medic'),
    path('medicos/eliminar_medic/<int:MedId>',eliminarMedic, name='eliminar_medic'),

    #Staff
    path('staff/', staff, name='staff'),
    path('staff/crear_staff', crearStaff, name='crear_staff'),
    path('staff/editar_staff/<int:StId>',editarStaff, name='editar_staff'),
    path('staff/eliminar_staff/<int:StId>',eliminarStaff, name='eliminar_staff'),


     path('importar/', importar_registros, name='importar_registros'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
