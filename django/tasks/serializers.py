from rest_framework import serializers
from .models import Task  # Importacion relativa — el punto significa "desde esta misma carpeta"

# Equivalente a un API Resource en Laravel (php artisan make:resource TaskResource)
# Transforma el modelo Task a JSON y viceversa
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # Meta es una clase interna de configuracion, similar a los $fillable/$casts en un modelo Laravel
        model = Task        # El modelo que serializa
        fields = '__all__'  # Expone todos los campos; se puede cambiar a una lista: ['id', 'title', 'completed']