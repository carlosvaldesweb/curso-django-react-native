# Programa Detallado: Django

## Progreso

| Sesion | Tema | Estado |
|---|---|---|
| 1 | Instalacion de Python y entorno de desarrollo | ✅ Completada (2026-03-11) |
| 2 | Crear proyecto Django y explorar la estructura | ✅ Completada (2026-03-11) |
| 3 | Modelos y migraciones | ✅ Completada (2026-03-11) |
| 4 | Django Admin | ✅ Completada |
| 5 | Configurar PostgreSQL | ✅ Completada |
| 6 | DRF: Serializers, Vistas, URLs y CRUD completo | ✅ Completada |
| 7 | Versionado de API + Modelo User + ForeignKey | ✅ Completada (2026-03-18) |
| 8 | JWT con simplejwt + Proteccion de endpoints | ✅ Completada (2026-03-18) |
| 9 | Endpoint de registro de usuarios | ⏳ Pendiente |
| 10 | Testing | ⏳ Pendiente |

---

## Sesion 1: Instalacion de Python y entorno de desarrollo

**Objetivos:**
- Instalar Python 3 (o verificar la version instalada)
- Entender que es `pip` (el Composer de Python)
- Crear un entorno virtual con `venv` (como tener un `vendor/` aislado por proyecto)
- Instalar Django dentro del entorno virtual

**Comparacion con Laravel:**
| Python/Django | PHP/Laravel |
|---|---|
| `python` | `php` |
| `pip` | `composer` |
| `venv` (entorno virtual) | No tiene equivalente directo (vendor es por proyecto pero PHP es global) |
| `pip install django` | `composer create-project laravel/laravel` |
| `requirements.txt` | `composer.json` |

---

## Sesion 2: Crear proyecto Django y explorar la estructura

**Objetivos:**
- Crear un proyecto Django con `django-admin startproject`
- Entender la estructura de archivos generada
- Crear una "app" Django (concepto clave: un proyecto tiene multiples apps)
- Ejecutar el servidor de desarrollo

**Comparacion con Laravel:**
| Django | Laravel |
|---|---|
| `django-admin startproject` | `composer create-project laravel/laravel` |
| `python manage.py runserver` | `php artisan serve` |
| `manage.py` | `artisan` |
| `settings.py` | `.env` + `config/` |
| Apps (modulos reutilizables) | No tiene equivalente directo (lo mas cercano son Packages) |
| `urls.py` | `routes/web.php`, `routes/api.php` |

---

## Sesion 3: Modelos y migraciones

**Objetivos:**
- Definir el modelo `Task` (titulo, descripcion, completada, fecha)
- Entender el ORM de Django
- Crear y ejecutar migraciones
- Interactuar con el modelo desde el shell de Django

**Comparacion con Laravel:**
| Django ORM | Eloquent (Laravel) |
|---|---|
| `models.py` | `app/Models/Task.php` |
| `models.CharField(max_length=200)` | `$table->string('title', 200)` |
| `models.BooleanField(default=False)` | `$table->boolean('completed')->default(false)` |
| `python manage.py makemigrations` | `php artisan make:migration` |
| `python manage.py migrate` | `php artisan migrate` |
| `Task.objects.all()` | `Task::all()` |
| `Task.objects.filter(completed=True)` | `Task::where('completed', true)->get()` |
| `python manage.py shell` | `php artisan tinker` |

---

## Sesion 4: Django Admin

**Objetivos:**
- Registrar el modelo `Task` en el admin
- Crear un superusuario
- Explorar y personalizar el panel de admin
- Agregar, editar y eliminar tareas desde el admin

**Comparacion con Laravel:**
Django Admin viene **incluido gratis**. En Laravel necesitas instalar paquetes como Nova (de pago) o Filament (gratuito). Esta es una de las grandes ventajas de Django.

---

## Sesion 5: Configurar PostgreSQL

**Objetivos:**
- Instalar PostgreSQL (si no esta instalado)
- Crear una base de datos para el proyecto
- Instalar `psycopg2` (driver de PostgreSQL para Python)
- Configurar la conexion en `settings.py`
- Migrar los datos a PostgreSQL

**Comparacion con Laravel:**
| Django + PostgreSQL | Laravel + MySQL |
|---|---|
| `settings.py` → `DATABASES` | `.env` → `DB_CONNECTION`, `DB_HOST`, etc. |
| `psycopg2` (driver) | `pdo_mysql` (extension PHP) |
| `python manage.py migrate` | `php artisan migrate` |
| PostgreSQL usa schemas | MySQL usa databases |

---

## Sesion 6: Django REST Framework - Serializers, Vistas, URLs y CRUD

**Objetivos:**
- Instalar Django REST Framework (DRF)
- Entender que son los Serializers
- Crear un serializer para el modelo `Task`
- Crear vistas con `ModelViewSet`
- Configurar URLs con el Router de DRF
- Probar el CRUD completo (GET, POST, PUT, PATCH, DELETE)

**Comparacion con Laravel:**
| DRF | Laravel |
|---|---|
| `serializers.py` | `app/Http/Resources/TaskResource.php` |
| `ModelSerializer` | `JsonResource` |
| `ModelViewSet` | Resource Controller + model binding |
| `urls.py` + `router` | `routes/api.php` |
| Navegador DRF (interfaz web) | Postman / Insomnia (externo) |

---

## Sesion 7: Versionado de API + Modelo User + ForeignKey

**Objetivos:**
- Versionar la API bajo `/api/v1/`
- Entender por que el versionado es critico en apps mobile
- Asociar tareas a usuarios con `ForeignKey`
- Filtrar tareas por usuario en `get_queryset`
- Excluir el campo `user` del serializer

**Nota importante:** En Laravel para web, casi nunca versionas la API porque el frontend (Blade/Nuxt) se actualiza al mismo tiempo. En mobile, es **obligatorio** porque no controlas cuando el usuario actualiza la app.

---

## Sesion 8: JWT con simplejwt + Proteccion de endpoints

**Objetivos:**
- Instalar `djangorestframework-simplejwt`
- Configurar endpoints para obtener y refrescar tokens
- Entender access token vs refresh token
- Proteger endpoints con `IsAuthenticated`
- Verificar que un usuario no puede acceder a tareas de otro

**Comparacion con Laravel:**
| Django + simplejwt | Laravel + Sanctum |
|---|---|
| JWT stateless — token NO vive en BD | Tokens stateful — viven en BD |
| Access + Refresh tokens | Token simple o JWT |
| `TokenObtainPairView` | `Auth::attempt()` + `createToken()` |
| `permission_classes = [IsAuthenticated]` | Middleware `auth:sanctum` |
| `get_queryset()` filtrado por usuario | Scopes en Eloquent |

---

## Sesion 9: Endpoint de registro de usuarios

**Objetivos:**
- Crear `POST /api/v1/auth/register/` sin autenticacion requerida
- Crear un serializer para registro (username, email, password)
- Hashear la contrasena correctamente con `create_user()`
- Devolver tokens JWT directamente al registrarse

**Comparacion con Laravel:**
| Django | Laravel |
|---|---|
| `create_user()` | `User::create()` con `Hash::make()` |
| `AllowAny` permission | Sin middleware `auth` en la ruta |

---

## Sesion 10: Testing

**Objetivos:**
- Escribir tests para los modelos
- Escribir tests para los endpoints de la API (con y sin token)
- Ejecutar tests con `python manage.py test`
- Entender `TestCase` y `APITestCase`

**Comparacion con Laravel:**
| Django Testing | Laravel Testing (PHPUnit) |
|---|---|
| `TestCase` | `TestCase` |
| `APITestCase` (DRF) | Feature tests con `actingAs()` |
| `self.assertEqual()` | `$this->assertEquals()` |
| `self.client.get()` | `$this->getJson()` |
| `python manage.py test` | `php artisan test` |
