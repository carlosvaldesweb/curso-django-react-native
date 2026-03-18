from rest_framework import serializers
from .models import Task  # Importacion relativa — el punto significa "desde esta misma carpeta"

# Equivalente a un API Resource en Laravel (php artisan make:resource TaskResource)
# Transforma el modelo Task a JSON y viceversa
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # Meta es una clase interna de configuracion, similar a los $fillable/$casts en un modelo Laravel
        model = Task        # El modelo que serializa
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at']  # Expone todos los campos en la vista para editar y mostrar, incluyendo id y timestamps