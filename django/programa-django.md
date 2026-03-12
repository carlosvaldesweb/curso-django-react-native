# Programa Detallado: Django

## Progreso

| Sesion | Estado |
|---|---|
| 1 | Completada (2026-03-11) |
| 2-13 | Pendiente |

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

## Sesion 6: Django REST Framework - Serializers

**Objetivos:**
- Instalar Django REST Framework (DRF)
- Entender que son los Serializers
- Crear un serializer para el modelo `Task`
- Entender la diferencia entre `Serializer` y `ModelSerializer`

**Comparacion con Laravel:**
| DRF Serializers | Laravel API Resources |
|---|---|
| `serializers.py` | `app/Http/Resources/TaskResource.php` |
| `ModelSerializer` | `JsonResource` |
| Valida datos de entrada Y formatea salida | Solo formatea salida (validacion va en FormRequest) |
| `serializer.is_valid()` | `$request->validate()` |

---

## Sesion 7: Vistas y URLs para API

**Objetivos:**
- Crear vistas basadas en clases (APIView, ViewSet)
- Configurar URLs para la API
- Entender los diferentes tipos de vistas en DRF
- Probar los endpoints con el navegador de DRF

**Comparacion con Laravel:**
| DRF | Laravel |
|---|---|
| `views.py` | `app/Http/Controllers/` |
| `urls.py` + `router` | `routes/api.php` |
| `APIView` | Controller con metodos individuales |
| `ViewSet` | Resource Controller (`--resource`) |
| `ModelViewSet` | Resource Controller + model binding |
| Navegador DRF (interfaz web) | Postman / Insomnia (externo) |

---

## Sesion 8: CRUD de tareas via API

**Objetivos:**
- Implementar el CRUD completo con un `ModelViewSet`
- Listar tareas (GET)
- Crear tarea (POST)
- Ver detalle de tarea (GET /:id)
- Actualizar tarea (PUT/PATCH /:id)
- Eliminar tarea (DELETE /:id)
- Probar todos los endpoints

---

## Sesion 9: Modelo User y autenticacion

**Objetivos:**
- Entender el modelo User de Django (viene incluido)
- Crear endpoint de registro de usuarios
- Asociar tareas a usuarios (ForeignKey)
- Actualizar migraciones

**Comparacion con Laravel:**
| Django | Laravel |
|---|---|
| `django.contrib.auth.models.User` (incluido) | `App\Models\User` (incluido) |
| `ForeignKey(User)` | `$table->foreignId('user_id')` |
| `create_user()` | `User::create()` con Hash |

---

## Sesion 10: JWT con simplejwt

**Objetivos:**
- Instalar `djangorestframework-simplejwt`
- Configurar endpoints para obtener y refrescar tokens
- Entender access token vs refresh token
- Probar el flujo de autenticacion

**Comparacion con Laravel:**
| Django + simplejwt | Laravel + Sanctum |
|---|---|
| JWT (stateless) | Tokens en BD (stateful) o JWT |
| Access + Refresh tokens | Token simple o JWT |
| `TokenObtainPairView` | `Auth::attempt()` + `createToken()` |
| Token en header `Authorization: Bearer ...` | Token en header `Authorization: Bearer ...` |

---

## Sesion 11: Permisos y proteccion de endpoints

**Objetivos:**
- Proteger endpoints para que solo usuarios autenticados accedan
- Filtrar tareas: cada usuario solo ve las suyas
- Entender `IsAuthenticated`, `IsOwner` (permisos custom)
- Probar acceso con y sin token

**Comparacion con Laravel:**
| Django DRF | Laravel |
|---|---|
| `permission_classes` | Middleware `auth:sanctum` |
| `IsAuthenticated` | `auth` middleware |
| Custom permissions | Gates y Policies |
| `get_queryset()` filtrado | Scopes en Eloquent |

---

## Sesion 12: Versionado de APIs

**Objetivos:**
- Entender por que el versionado es critico en apps mobile
- Diferencia con web: en web el frontend se despliega junto con el backend, en mobile los usuarios pueden tener versiones antiguas de la app
- Estrategias de versionado: URL path (`/api/v1/`), headers, query params
- Implementar versionado por URL en DRF
- Organizar el codigo para multiples versiones

**Nota importante:** En Laravel para web, casi nunca versionas la API porque el frontend (Blade/Nuxt) se actualiza al mismo tiempo. En mobile, es **obligatorio** porque no controlas cuando el usuario actualiza la app.

---

## Sesion 13: Testing

**Objetivos:**
- Escribir tests para los modelos
- Escribir tests para los endpoints de la API
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
