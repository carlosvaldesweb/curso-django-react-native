# Sesión 2: Crear proyecto Django y explorar la estructura

**Fecha:** 2026-03-11

## Objetivos

- [x] Crear un proyecto Django con `django-admin startproject`
- [x] Entender la estructura de archivos generada
- [x] Crear una app Django (`tasks`)
- [x] Registrar la app en `INSTALLED_APPS`
- [x] Ejecutar el servidor de desarrollo

## Resumen

Se creó el proyecto Django y la primera app:

1. Se creó el proyecto **todoproject** con `django-admin startproject todoproject .` (el punto evita una carpeta anidada extra)
2. Se exploró la estructura generada: `manage.py` (el `artisan` de Django) y `todoproject/` (carpeta de configuración)
3. Se ejecutó el servidor de desarrollo con `python manage.py runserver` en `http://127.0.0.1:8000/`
4. Se creó la app **tasks** con `python manage.py startapp tasks`
5. Se registró la app en `INSTALLED_APPS` dentro de `settings.py`

## Comparaciones con Laravel

| Django | Laravel |
|---|---|
| `django-admin startproject todoproject .` | `composer create-project laravel/laravel` |
| `manage.py` | `artisan` |
| `python manage.py runserver` | `php artisan serve` |
| `settings.py` (todo en un archivo) | `.env` + carpeta `config/` |
| `urls.py` | `routes/web.php`, `routes/api.php` |
| `python manage.py startapp tasks` | `php artisan make:model Task -mcr` (parcial) |
| Registrar app en `INSTALLED_APPS` | Registrar ServiceProvider (Laravel antiguo) |
| Proyecto → tiene muchas Apps | No tiene equivalente directo (lo más cercano: Packages) |

### Concepto clave: Proyecto vs App

- **Proyecto** = contenedor general + configuración. Solo hay uno.
- **App** = módulo con modelos, vistas, rutas. Puede haber muchas. Son reutilizables entre proyectos.

En Laravel todo vive junto en una sola estructura. En Django se separa en apps modulares.

## Estructura generada

```
django/
├── manage.py                  # CLI de Django (como artisan)
├── todoproject/               # Configuración del proyecto
│   ├── __init__.py            # Marca la carpeta como paquete Python
│   ├── settings.py            # TODA la configuración
│   ├── urls.py                # Rutas principales
│   ├── wsgi.py                # Entry point producción (sync)
│   └── asgi.py                # Entry point producción (async)
├── tasks/                     # App de tareas
│   ├── __init__.py
│   ├── admin.py               # Config del panel admin
│   ├── apps.py                # Metadata de la app
│   ├── models.py              # Modelos (ORM)
│   ├── views.py               # Vistas/controladores
│   ├── tests.py               # Tests
│   └── migrations/            # Migraciones de BD
└── db.sqlite3                 # Base de datos SQLite (default)
```

## Comandos clave

```bash
# Crear proyecto Django (el punto = en directorio actual)
django-admin startproject todoproject .

# Ejecutar servidor de desarrollo
python manage.py runserver

# Crear una app
python manage.py startapp tasks
```

## Archivos clave de settings.py

| Sección | Qué hace | Equivalente Laravel |
|---|---|---|
| `SECRET_KEY` | Clave secreta del proyecto | `APP_KEY` en `.env` |
| `DEBUG` | Modo debug | `APP_DEBUG` en `.env` |
| `INSTALLED_APPS` | Apps registradas | `providers` en `config/app.php` |
| `DATABASES` | Configuración de BD (SQLite por defecto) | `config/database.php` + `.env` |
| `MIDDLEWARE` | Middleware del proyecto | `app/Http/Kernel.php` |

## Notas adicionales

- Django usa **SQLite** por defecto. Lo cambiaremos a PostgreSQL en la sesión 5.
- Al ejecutar `runserver`, Django avisó de 18 migraciones pendientes — son de las apps internas (`admin`, `auth`, `sessions`). Se aplicarán en la siguiente sesión.
- Las apps no traen `urls.py` por defecto — hay que crearlo manualmente cuando se necesite.
