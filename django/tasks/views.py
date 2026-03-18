from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

# Equivalente a un Resource Controller en Laravel (php artisan make:controller TaskController --resource)
# ModelViewSet genera automaticamente los 5 endpoints CRUD:
#   list (GET /tasks/), create (POST /tasks/),
#   retrieve (GET /tasks/{id}/), update (PUT /tasks/{id}/), destroy (DELETE /tasks/{id}/)
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer   # Que serializer usar para transformar los datos a JSON

    # Esto es equivalente al método:
    # public function index(Request $request) {
    #   return $request->user()->tasks; // Solo devuelve las tareas del usuario autenticado
    # }
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Task.objects.none()  # Si no hay usuario autenticado, devuelve un queryset vacío
        return Task.objects.filter(user=self.request.user)  # Solo devuelve las tareas del usuario autenticado

    # Equivalente en laravel a 
    # public function store(Request $request) {
    #   $request->user()->tasks()->create($request->validated());
    # }
    def perform_create(self, serializer):
        # Ternario en Python: "valor_si_true if condicion else valor_si_false"
        # En JS seria: this.request.user.is_authenticated ? this.request.user : null
        # None es el equivalente de null en Python
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)  # Asocia la tarea al usuario autenticado, o None si no hay sesion