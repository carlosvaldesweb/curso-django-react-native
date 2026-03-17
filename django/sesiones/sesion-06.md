# Sesión 6 - Django REST Framework: Primera API

**Fecha:** 2026-03-17

## Objetivos

- Instalar y configurar Django REST Framework (DRF)
- Crear el primer serializer
- Crear un ViewSet con CRUD completo
- Configurar el Router para generar URLs automáticamente
- Probar la API con el Browsable API de DRF

## Resumen de lo aprendido

En esta sesión construimos la primera API REST funcional del proyecto. Con muy poco código (menos de 20 líneas en total) obtuvimos un CRUD completo para el modelo `Task`.

### Archivos creados/modificados

| Archivo | Acción | Descripción |
|---|---|---|
| `tasks/serializers.py` | Creado | Serializer del modelo Task |
| `tasks/views.py` | Modificado | ViewSet con CRUD completo |
| `tasks/urls.py` | Creado | Router con URLs automáticas |
| `todoproject/urls.py` | Modificado | Montaje de la API bajo `/api/` |
| `todoproject/settings.py` | Modificado | Registro de `rest_framework` en `INSTALLED_APPS` |

## Comparaciones con Laravel/Vue

| Concepto Django/DRF | Equivalente Laravel |
|---|---|
| `ModelSerializer` | `JsonResource` (API Resource) |
| `ModelViewSet` | Resource Controller (`--resource`) |
| `DefaultRouter` | `Route::apiResource()` |
| `INSTALLED_APPS` | Service Provider en `config/app.php` |
| `psycopg` (driver BD) | Extensión PHP `pdo_pgsql` |
| Import relativo (`from .models`) | No existe en PHP — namespaces siempre absolutos |

## Comandos clave

```bash
# Instalar DRF
pip install djangorestframework

# Actualizar requirements
pip freeze > requirements.txt
```

## Código clave

### serializers.py
```python
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
```

### views.py
```python
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
```

### tasks/urls.py
```python
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls
```

### todoproject/urls.py
```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
]
```

## Endpoints generados automáticamente

| Método | URL | Acción |
|---|---|---|
| GET | `/api/tasks/` | Listar todas las tareas |
| POST | `/api/tasks/` | Crear tarea |
| GET | `/api/tasks/{id}/` | Ver detalle de una tarea |
| PUT | `/api/tasks/{id}/` | Actualizar tarea completa |
| PATCH | `/api/tasks/{id}/` | Actualizar campos parciales |
| DELETE | `/api/tasks/{id}/` | Eliminar tarea |

## Conceptos aclarados durante la sesión

- **`INSTALLED_APPS` vs driver de BD**: `rest_framework` se registra en `INSTALLED_APPS` porque tiene templates, comandos y configuración. `psycopg` no, porque es solo un driver interno.
- **Imports relativos**: El `.` en `from .models import Task` significa "desde esta misma carpeta". Conveniente para referencias internas dentro de una app.
- **Raw strings (`r''`)**: La `r` antes de un string evita que Python interprete caracteres especiales. Con "tasks" no hay diferencia, pero es convención en patrones de URL/regex.
- **DRF**: Acrónimo de Django REST Framework.
- **Browsable API**: Interfaz web que DRF genera automáticamente en desarrollo para explorar y probar endpoints sin Postman.

## Notas adicionales

- El Browsable API solo debe usarse en desarrollo. En producción se puede desactivar.
- `fields = '__all__'` expone todos los campos del modelo. En sesiones futuras aprenderemos a limitar qué campos se exponen (importante para no filtrar datos sensibles).
- Próximo paso: autenticación con JWT y versionado de la API (`/api/v1/`).
