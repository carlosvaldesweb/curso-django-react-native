from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

# Equivalente a un Resource Controller en Laravel (php artisan make:controller TaskController --resource)
# ModelViewSet genera automaticamente los 5 endpoints CRUD:
#   list (GET /tasks/), create (POST /tasks/),
#   retrieve (GET /tasks/{id}/), update (PUT /tasks/{id}/), destroy (DELETE /tasks/{id}/)
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()       # Consulta base — equivalente a Task::all() en Eloquent
    serializer_class = TaskSerializer   # Que serializer usar para transformar los datos a JSON