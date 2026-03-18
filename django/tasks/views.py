from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

# Equivalente a un Resource Controller en Laravel (php artisan make:controller TaskController --resource)
# ModelViewSet genera automaticamente los 5 endpoints CRUD:
#   list (GET /tasks/), create (POST /tasks/),
#   retrieve (GET /tasks/{id}/), update (PUT /tasks/{id}/), destroy (DELETE /tasks/{id}/)
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer   # Que serializer usar para transformar los datos a JSON

    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder a estos endpoints

    # Esto es equivalente al método:
    # public function index(Request $request) {
    #   return $request->user()->tasks; // Solo devuelve las tareas del usuario autenticado
    # }
    def get_queryset(self):
        # Gracias a permission_classes = [IsAuthenticated], aquí el usuario SIEMPRE está autenticado
        # self.request.user es equivalente a Auth::user() en Laravel o $auth.user en Vue
        return Task.objects.filter(user=self.request.user)

        # Patrón alternativo (útil si NO tuvieras permission_classes):
        # if not self.request.user.is_authenticated:
        #     return Task.objects.none()  # none() devuelve queryset vacío — equivalente a collect([]) en Laravel
        # return Task.objects.filter(user=self.request.user)

    # Equivalente en Laravel a:
    # public function store(Request $request) {
    #   $request->user()->tasks()->create($request->validated());
    # }
    def perform_create(self, serializer):
        # serializer.save(user=...) inyecta el campo user antes de guardar en BD
        # Equivalente a $task->user()->associate(Auth::user()) en Laravel
        serializer.save(user=self.request.user)

        # Patrón alternativo (útil si NO tuvieras permission_classes):
        # Ternario en Python: "valor_si_true if condicion else valor_si_false"
        # En JS sería: this.request.user.is_authenticated ? this.request.user : null
        # None es el equivalente de null en Python
        # user = self.request.user if self.request.user.is_authenticated else None
        # serializer.save(user=user)