# Sesión 7 - Versionado de API y Modelo User

**Fecha:** 2026-03-18

## Objetivos

- Versionar la API bajo `/api/v1/`
- Asociar tareas a usuarios con `ForeignKey`
- Filtrar tareas por usuario autenticado
- Excluir el campo `user` del serializer

## Resumen de lo aprendido

En esta sesión hicimos dos cosas: versionamos la API (cambio mínimo pero crítico para apps mobile) y preparamos la relación entre `Task` y `User` para cuando llegue la autenticación real con JWT.

### Archivos modificados

| Archivo | Cambio |
|---|---|
| `todoproject/urls.py` | Cambio de `/api/` a `/api/v1/` |
| `tasks/models.py` | Agregado `ForeignKey` a `User` |
| `tasks/serializers.py` | `fields = '__all__'` reemplazado por lista explícita sin `user` |
| `tasks/views.py` | Agregados `get_queryset` y `perform_create` |
| `tasks/urls.py` | Agregado `basename='task'` al router |
| `tasks/migrations/0002_task_user.py` | Migración: agrega campo `user` obligatorio |
| `tasks/migrations/0003_alter_task_user.py` | Migración: cambia `user` a nullable |

## Comparaciones con Laravel/Vue

| Concepto Django/DRF | Equivalente Laravel |
|---|---|
| `ForeignKey('auth.User', ...)` | `$table->foreignId('user_id')->constrained()` |
| `on_delete=models.CASCADE` | `->onDelete('cascade')` |
| `related_name='tasks'` | `hasMany(Task::class)` en el modelo User |
| `'auth.User'` | `App\Models\User` |
| `python manage.py makemigrations` | `php artisan make:migration` (pero Django detecta los cambios automáticamente) |
| `Task.objects.none()` | `collect()` vacío / `Task::whereRaw('1=0')->get()` |
| `Task.objects.filter(user=...)` | `Task::where('user_id', auth()->id())->get()` |
| `perform_create` | Lógica en el método `store()` del controller |
| `get_queryset` | Lógica en el método `index()` del controller |

## Código clave

### Versionado en todoproject/urls.py
```python
path('api/v1/', include('tasks.urls'))  # Solo cambiar 'api/' por 'api/v1/'
```

### ForeignKey en models.py
```python
user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
```

### Serializer con campos explícitos
```python
fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at']
# user se excluye para que no aparezca en el formulario — se asigna automáticamente
```

### Filtrado y creación en views.py
```python
def get_queryset(self):
    if not self.request.user.is_authenticated:
        return Task.objects.none()
    return Task.objects.filter(user=self.request.user)

def perform_create(self, serializer):
    user = self.request.user if self.request.user.is_authenticated else None
    serializer.save(user=user)
```

### basename en urls.py
```python
router.register(r'tasks', TaskViewSet, basename='task')
# Necesario cuando el ViewSet no tiene atributo queryset (usa get_queryset en su lugar)
```

## Conceptos aclarados durante la sesión

- **Versionado de API**: En web el frontend se despliega junto con el backend. En mobile, los usuarios pueden tener versiones antiguas de la app durante semanas — versionar la API (`/api/v1/`) permite hacer cambios breaking en `v2` sin romper las apps antiguas.
- **`None` vs `null`**: En Python no existe `null`. El equivalente es `None` (con N mayúscula).
- **Ternario en Python**: La sintaxis es `valor_si_true if condicion else valor_si_false` — al revés que en JS (`condicion ? true : false`).
- **`makemigrations` automático**: A diferencia de Laravel donde `make:migration` crea un archivo vacío, Django compara el modelo actual con el estado anterior y genera el archivo de migración automáticamente.
- **`basename` en el router**: Cuando se usa `get_queryset()` en lugar del atributo `queryset`, el Router no puede deducir el nombre base — hay que especificarlo con `basename='task'`.

## Notas adicionales

- El campo `user` está como `null=True, blank=True` temporalmente. Cuando implementemos JWT, lo haremos obligatorio y siempre se asignará desde el token.
- Próximo paso: autenticación con JWT usando `djangorestframework-simplejwt`.
