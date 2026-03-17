# Sesion 4: Django Admin

**Fecha:** 2026-03-17

## Objetivos

- [x] Registrar el modelo `Task` en el admin
- [x] Crear un superusuario
- [x] Explorar y personalizar el panel de admin
- [x] Agregar, editar y eliminar tareas desde el admin

## Resumen

1. Se creo un **superusuario** con `python manage.py createsuperuser` para acceder al panel de administracion en `/admin/`
2. Se registro el modelo `Task` en `tasks/admin.py` usando `admin.site.register(Task)`
3. Se creo la clase `TaskAdmin` heredando de `admin.ModelAdmin` para personalizar el admin
4. Se configuraron tres propiedades de personalizacion:
   - `list_display`: columnas visibles en la lista (`title`, `description`, `completed`, `created_at`)
   - `list_filter`: panel lateral para filtrar por `completed`
   - `search_fields`: barra de busqueda por `title`
5. Se aprendio que las tuplas de un solo elemento en Python requieren coma al final: `('campo',)`

## Comparaciones con Laravel

### Django Admin vs Laravel

Django Admin viene **incluido de serie** y es completamente funcional con solo registrar el modelo. En Laravel necesitas instalar paquetes externos:
- **Nova** (pago, oficial de Laravel)
- **Filament** (gratuito, muy popular)

Esta es una de las grandes ventajas de Django para proyectos que necesitan un backoffice rapido.

### Equivalencias

| Django Admin | Laravel (Filament/Nova) |
|---|---|
| `admin.site.register(Task)` | Registrar recurso en el panel |
| `list_display` | Columnas en la tabla del listado |
| `list_filter` | Filtros laterales |
| `search_fields` | Barra de busqueda |
| `admin.ModelAdmin` | Clase Resource de Filament |
| `python manage.py createsuperuser` | `php artisan make:user` (o manual) |

## Sintaxis de Python aprendida

### Tuplas con un solo elemento

En Python, los parentesis solos no crean una tupla — necesitas la coma final:

```python
# ❌ Esto es solo un string entre parentesis
list_filter = ('completed')

# ✅ Esto es una tupla de un elemento
list_filter = ('completed',)
```

En PHP/JavaScript no existe este concepto — los arrays de un elemento son normales:
```php
// PHP: no hay ambiguedad
$filter = ['completed'];
```

### Herencia de clases

```python
# Django: heredar de admin.ModelAdmin
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
```

Equivalente conceptual en Laravel (Filament):
```php
class TaskResource extends Resource {
    // configuracion del recurso
}
```

## Codigo clave

```python
# tasks/admin.py

from django.contrib import admin
from tasks.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created_at')
    list_filter = ('completed',)
    search_fields = ('title',)

admin.site.register(Task, TaskAdmin)
```

## Comandos clave

```bash
# Crear superusuario para acceder al admin
python manage.py createsuperuser

# Iniciar el servidor
python manage.py runserver

# URL del admin
http://127.0.0.1:8000/admin/
```

## Notas adicionales

- El admin de Django es ideal para desarrollo y para clientes que necesitan gestionar datos sin interfaz personalizada
- `list_display` no acepta campos con `auto_now=True` para ordenar, pero si para mostrar
- La URL `/admin/` esta configurada por defecto en `urls.py` del proyecto — no hay que hacer nada extra
