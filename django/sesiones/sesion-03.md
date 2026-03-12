# Sesion 3: Modelos y migraciones

**Fecha:** 2026-03-11

## Objetivos

- [x] Definir el modelo `Task` (titulo, descripcion, completada, fecha)
- [x] Entender el ORM de Django
- [x] Crear y ejecutar migraciones
- [x] Interactuar con el modelo desde el shell de Django

## Resumen

1. Se definio el modelo **Task** en `tasks/models.py` con 5 campos: `title`, `description`, `completed`, `created_at`, `updated_at`
2. Se genero la migracion automaticamente con `python manage.py makemigrations`
3. Se ejecutaron todas las migraciones pendientes con `python manage.py migrate` (18 de Django + 1 nuestra)
4. Se uso el **shell de Django** (`python manage.py shell`) para crear, leer, actualizar y eliminar tareas
5. Se configuraron las extensiones de VS Code (Python + Pylance) para tener autocompletado

## Comparaciones con Laravel

### Modelo: Django vs Eloquent

| Concepto | Django | Laravel |
|---|---|---|
| Archivo del modelo | `tasks/models.py` | `app/Models/Task.php` |
| Definicion de campos | En el modelo directamente | En la migracion (separado del modelo) |
| Generar migracion | `python manage.py makemigrations` (automatico) | `php artisan make:migration` (manual) |
| Ejecutar migraciones | `python manage.py migrate` | `php artisan migrate` |
| Consola interactiva | `python manage.py shell` | `php artisan tinker` |

### Tipos de campo: Django vs Laravel (migracion)

| Django | Laravel (migracion) | Notas |
|---|---|---|
| `CharField(max_length=200)` | `$table->string('campo', 200)` | Texto corto, longitud obligatoria |
| `TextField()` | `$table->text('campo')` | Texto largo, sin limite |
| `BooleanField(default=False)` | `$table->boolean('campo')->default(false)` | Verdadero/falso |
| `DateTimeField(auto_now_add=True)` | `$table->timestamps()` (created_at) | Se asigna solo al crear |
| `DateTimeField(auto_now=True)` | `$table->timestamps()` (updated_at) | Se actualiza en cada save() |
| `IntegerField()` | `$table->integer('campo')` | Numero entero |
| `DecimalField()` | `$table->decimal('campo')` | Numero decimal |
| `ForeignKey()` | `$table->foreignId('campo')` | Relacion con otro modelo |
| `id` (automatico) | `$table->id()` (automatico) | Django agrega id autoincremental |

### Opciones comunes de campos

| Django | Laravel | Significado |
|---|---|---|
| `default=valor` | `->default(valor)` | Valor por defecto |
| `blank=True` | `->nullable()` (en validacion) | Permite vacio en formularios/validaciones |
| `null=True` | `->nullable()` (en BD) | Permite NULL en la base de datos |
| `max_length=N` | Segundo parametro de `string()` | Longitud maxima |

### ORM: Consultas Django vs Eloquent

| Operacion | Django | Laravel (Eloquent) |
|---|---|---|
| Obtener todos | `Task.objects.all()` | `Task::all()` |
| Crear | `Task.objects.create(title="...")` | `Task::create(['title' => '...'])` |
| Filtrar | `Task.objects.filter(completed=True)` | `Task::where('completed', true)->get()` |
| Obtener uno por id | `Task.objects.get(id=1)` | `Task::find(1)` |
| Guardar cambios | `task.save()` | `$task->save()` |
| Eliminar | `task.delete()` | `$task->delete()` |
| Acceder a propiedad | `task.title` | `$task->title` |

## Sintaxis basica de Python aprendida

| Concepto | PHP | Python |
|---|---|---|
| Definir clase | `class Task extends Model { }` | `class Task(models.Model):` |
| Herencia | `extends` | Parentesis: `(ClasePadre)` |
| Bloques de codigo | `{ }` | `:` + indentacion (4 espacios) |
| Propiedades | `$this->title` | `self.title` |
| Variables | `$task = ...` | `task = ...` (sin $) |
| Metodos | `public function nombre()` | `def nombre(self):` |
| toString | `__toString()` | `__str__(self)` |
| Fin de linea | `;` | Nada |
| Imports | `use App\Models\Task;` | `from tasks.models import Task` |

## Comandos clave

```bash
# Generar migracion automaticamente desde el modelo
python manage.py makemigrations

# Ejecutar migraciones pendientes
python manage.py migrate

# Abrir shell interactivo (como tinker)
python manage.py shell

# Dentro del shell:
from tasks.models import Task
Task.objects.all()
Task.objects.create(title="Mi tarea")
task = Task.objects.get(id=1)
task.completed = True
task.save()
task.delete()
```

## Configuracion VS Code

- Extension **Python** (Microsoft) + **Pylance**: autocompletado, ir a definicion, deteccion de errores
- Configurar interprete: `Cmd + Shift + P` > "Python: Select Interpreter" > seleccionar el de `venv/bin/python`

## Notas adicionales

- Django nombra las tablas como `nombreapp_modelo` (ej: `tasks_task`). En Laravel seria solo `tasks`.
- A diferencia de Laravel, en Django el modelo y la estructura de la tabla se definen en el mismo lugar. No hay migracion separada — Django la genera automaticamente al leer tu modelo.
- La base de datos actual es SQLite (el default). Se cambiara a PostgreSQL en la sesion 5.
