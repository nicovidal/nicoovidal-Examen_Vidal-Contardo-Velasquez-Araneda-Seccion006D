from rest_framework import serializers
from .models import FundacionMiembro, Planta

class PlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Planta
        fields=['id','nombrePlanta','imagenPlanta','nombreCientifico','ubicacion','descripcion']

class miembrosSerializer(serializers.ModelSerializer):
    class Meta:
        model=FundacionMiembro
        fields=['idMiembro','ID_Usuario']