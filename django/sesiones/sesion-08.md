# Sesión 8 - JWT y Protección de Endpoints

**Fecha:** 2026-03-18

---

## Objetivos

- Instalar y configurar `djangorestframework-simplejwt`
- Entender access token vs refresh token
- Crear endpoints de login y refresh
- Proteger endpoints con `IsAuthenticated`
- Filtrar tareas por usuario autenticado

---

## Resumen

En esta sesión completamos el sistema de autenticación JWT y la protección de la API. A partir de ahora, ningún endpoint de tasks es accesible sin un token válido, y cada usuario solo ve sus propias tareas.

---

## Lo que hicimos

### 1. Instalar simplejwt
```bash
pip install djangorestframework-simplejwt
```

### 2. Configurar en settings.py
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',  # OJO: con coma separados
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

> **Nota Python:** Las tuplas `()` son inmutables (no cambian), las listas `[]` son mutables. DRF usa tuplas en su configuración como convención para indicar que no deben modificarse en runtime. Ambas funcionan igual aquí.

### 3. Agregar endpoints en urls.py
```python
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

path('api/v1/auth/token/', TokenObtainPairView.as_view()),
path('api/v1/auth/token/refresh/', TokenRefreshView.as_view()),
```

### 4. Proteger y filtrar en views.py
```python
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

---

## Flujo JWT completo

```
1. POST /api/v1/auth/token/          → manda username+password → recibe access + refresh
2. GET  /api/v1/tasks/               → Authorization: Bearer <access>
3. access expira (5 min por defecto)...
4. POST /api/v1/auth/token/refresh/  → manda refresh → recibe nuevo access
5. Repite desde el paso 2
6. refresh expira (1 día) → el usuario debe hacer login de nuevo
```

- **access token** → para hacer peticiones. Dura poco (5 min) por seguridad
- **refresh token** → solo para renovar el access. No se usa para peticiones a la API

---

## Comparaciones con Laravel/Sanctum

| Django + simplejwt | Laravel + Sanctum |
|---|---|
| JWT stateless — token NO vive en BD | Tokens stateful — viven en BD (tabla `personal_access_tokens`) |
| Revocar al instante: difícil (hay que esperar que expire) | Revocar al instante: fácil (borra el registro) |
| Escala mejor (sin consulta a BD por petición) | Consulta BD en cada petición |
| Dos tokens: access + refresh | Un token simple (o JWT si se configura) |
| `TokenObtainPairView` | `Auth::attempt()` + `createToken()` |
| `permission_classes = [IsAuthenticated]` | Middleware `auth:sanctum` en rutas |
| `get_queryset()` con filter | Scopes en Eloquent o `Auth::user()->tasks()` |
| `self.request.user` | `Auth::user()` / `$request->user()` |

**Sanctum modo SPA (cookies):** para Nuxt/Vue en el mismo dominio, usa cookies httpOnly con CSRF — más seguro contra XSS. Para mobile siempre JWT.

---

## Pruebas con curl

```bash
# Login
curl -X POST http://localhost:8000/api/v1/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "carlosvaldes", "password": "password"}'

# Usar el access token
curl http://localhost:8000/api/v1/tasks/ \
  -H "Authorization: Bearer <access_token>"

# Sin token → 401 Authentication credentials were not provided.
curl http://localhost:8000/api/v1/tasks/

# Renovar access token
curl -X POST http://localhost:8000/api/v1/auth/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "<refresh_token>"}'
```

---

## Comandos clave

```bash
pip install djangorestframework-simplejwt
python manage.py runserver
python manage.py createsuperuser
python manage.py changepassword <username>
```

---

## Configuración de VSCode recomendada

Para evitar tener que seleccionar el intérprete manualmente cada vez, crear `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python"
}
```

---

## Próxima sesión

- Endpoint de **registro de usuarios** (POST /api/v1/auth/register/)
- Personalizar la respuesta del token (agregar nombre, email al payload)
- Comenzar con React Native / Expo
