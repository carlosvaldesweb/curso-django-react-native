from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# DefaultRouter es el equivalente a Route::apiResource('tasks', TaskController::class) en Laravel
# Genera automaticamente todas las rutas CRUD para el ViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')  # r'' es un raw string — convencion para patrones de URL/regex

# router.urls contiene todas las URLs generadas automaticamente por el router
urlpatterns = router.urls