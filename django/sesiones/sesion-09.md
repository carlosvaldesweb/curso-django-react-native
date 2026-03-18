# Sesión 9 - Modelo User personalizado + Endpoint de registro

**Fecha:** 2026-03-18

---

## Objetivos

- Crear una app `users` con modelo User personalizado (email como identificador, sin username)
- Entender por qué Django requiere un UserManager personalizado
- Crear el endpoint `POST /api/v1/auth/register/` que devuelve tokens JWT al registrarse
- Actualizar el login para usar email en vez de username

---

## Resumen

En esta sesión eliminamos el `username` del modelo User y dejamos el email como único identificador. Esto requirió crear una app `users` separada, definir un `UserManager` personalizado, y resetear las migraciones. Al final el flujo completo funciona: registro con email+password devuelve tokens JWT listos para usar.

---

## Lo que hicimos

### 1. Crear la app users
```bash
python manage.py startapp users
```

### 2. Modelo User personalizado (users/models.py)
```python
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # hashea con bcrypt — nunca asignes password directamente
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
```

### 3. Configurar en settings.py
```python
INSTALLED_APPS = [..., 'users']
AUTH_USER_MODEL = 'users.User'
```

### 4. Actualizar ForeignKey en tasks/models.py
```python
from django.conf import settings
user = models.ForeignKey(settings.AUTH_USER_MODEL, ...)
```

### 5. Reset de migraciones y BD
```bash
rm tasks/migrations/0001_initial.py tasks/migrations/0002_task_user.py tasks/migrations/0003_alter_task_user.py
psql -h 127.0.0.1 -p 54321 -U postgres -c "DROP DATABASE tododb;"
psql -h 127.0.0.1 -p 54321 -U postgres -c "CREATE DATABASE tododb;"
python manage.py makemigrations
python manage.py migrate
```

### 6. Serializer de registro (users/serializers.py)
```python
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # entra pero nunca sale

    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(...)
```

### 7. Vista de registro (users/views.py)
```python
class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]  # endpoint público
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        # valida, crea usuario, genera tokens y los devuelve en la respuesta
```

### 8. URLs
```python
# users/urls.py
path('register/', RegisterView.as_view()),

# todoproject/urls.py
path('api/v1/auth/', include('users.urls')),
```

---

## Conceptos clave

### Por qué se necesita UserManager
El `UserManager` por defecto de Django espera `username`. Al eliminarlo, Django no sabe cómo crear usuarios — necesita instrucciones explícitas. El manager centraliza esa lógica.

### fields vs write_only/read_only en serializers
- `fields` — define qué campos **participan** en el serializer (entrada y/o salida). Como `$fillable` en Laravel.
- `write_only=True` — solo entra en el request, nunca sale. Como `$hidden` en Laravel.
- `read_only=True` — solo sale en la respuesta, nunca entra.

### Dos métodos create()
- `create()` en el **serializer** — sabe cómo construir el objeto (fábrica)
- `create()` en la **vista** — orquesta el request HTTP y decide qué devolver

### as_view()
Django espera funciones en las URLs. `as_view()` convierte una clase en función.

### Por qué Django no tiene migrate:fresh por defecto
No existe en Django puro, pero se puede instalar `django-extensions` que agrega `reset_db`.

---

## Comparaciones con Laravel

| Django | Laravel |
|---|---|
| `AbstractUser` + `UserManager` | Extender `User` model |
| `USERNAME_FIELD = 'email'` | Cambiar `'username'` en `config/auth.php` |
| `user.set_password()` | `Hash::make($password)` |
| `get_user_model()` | `config('auth.providers.users.model')` |
| `serializer.is_valid(raise_exception=True)` | `$request->validate([...])` |
| `permissions.AllowAny` | Ruta sin middleware `auth` |
| `RefreshToken.for_user(user)` | `$user->createToken()` en Sanctum |
| `generics.CreateAPIView` | Controlador con solo `store()` |
| Serializer (valida + transforma + guarda) | FormRequest + Resource + Model |

---

## Pruebas con curl

```bash
# Registro — crea usuario y devuelve tokens JWT listos para usar
curl -X POST http://localhost:8000/api/v1/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"email": "carlos@test.com", "password": "123456"}'

# Login con email
curl -X POST http://localhost:8000/api/v1/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"email": "carlos@test.com", "password": "123456"}'
```

---

## Próxima sesión

- Comenzar con **React Native / Expo**
- Crear el proyecto mobile
- Explorar la estructura y hacer funcionar "Hello World"
