# Rutas de autenticación de la app users.
# A diferencia de tasks (que usa DefaultRouter para CRUD completo),
# aquí registramos rutas individuales porque no es un recurso REST estándar.
# Equivalente a Route::post('/register', [AuthController::class, 'register']) en Laravel.
from django.urls import path
from .views import RegisterView

urlpatterns = [
    # POST /api/v1/auth/register/ → crea usuario y devuelve tokens JWT
    # as_view() convierte la clase RegisterView en una función que Django puede llamar.
    path('register/', RegisterView.as_view()),
]
