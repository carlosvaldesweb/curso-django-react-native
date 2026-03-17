from django.contrib import admin
from tasks.models import Task


# Equivalente a una clase Resource en Filament (Laravel) o Nova
# Django Admin viene incluido — en Laravel necesitas instalar Filament o Nova
class TaskAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista — como definir columnas en la tabla de Filament
    list_display = ('title', 'description', 'completed', 'created_at')

    # Panel lateral de filtros — como los filtros en Filament
    list_filter = ('completed',)

    # Barra de busqueda — busca en los campos indicados
    search_fields = ('title',)


# Registrar el modelo con su configuracion de admin
# Sin TaskAdmin seria: admin.site.register(Task) — admin basico sin personalizacion
admin.site.register(Task, TaskAdmin)