from numpy import cumprod
from rest_framework import serializers
from .models import Equipo, Jugadores, Cuerpo_técnico

class Equipo_serializers(serializers.ModelSerializer):
    
    Nombre_Equipo = serializers.CharField(max_length=100)
    Imagen = serializers.CharField(max_length=200) 
    Escudo = serializers.CharField(max_length=200)

    class Meta:
        model = Equipo
        fields = '__all__'    

class Jugadores_serializers(serializers.ModelSerializer):

    idEquipo= serializers.IntegerField()
    Foto= serializers.CharField(max_length=200) 
    Nombre= serializers.CharField(max_length=200)
    Apellido= serializers.CharField(max_length=200)
    Fnacimiento= serializers.CharField(max_length=200)
    Edad = serializers.IntegerField()
    Posición= serializers.CharField(max_length=200)
    NCamiseta= serializers.CharField(max_length=200)
    titular= serializers.CharField(max_length=200)

    class Meta:
        model = Jugadores
        fields = '__all__'  


class Cuerpo_técnico_serializers(serializers.ModelSerializer):

    Nombre=serializers.CharField(max_length=200) 
    Apellido=serializers.CharField(max_length=200) 
    FNacimiento=serializers.CharField(max_length=200)
    Nacionalidad=serializers.CharField(max_length=200) 
    Rol = serializers.CharField(max_length=200) 

    class Meta:
        model = Cuerpo_técnico
        fields = '__all__'      