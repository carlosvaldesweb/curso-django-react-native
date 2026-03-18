from django.db import models

# En Laravel: app/Models/Task.php + migration create_tasks_table
# En Django el modelo Y la estructura de la tabla se definen juntos aqui
# Django genera la migracion automaticamente con: python manage.py makemigrations

class Task(models.Model):
    # CharField = $table->string('title', 200)
    title = models.CharField(max_length=200)
    # TextField = $table->text('description') | blank=True permite vacio en validaciones
    description = models.TextField(blank=True, default="")
    # BooleanField = $table->boolean('completed')->default(false)
    completed = models.BooleanField(default=False)
    # ForeignKey = $table->foreignId('user_id')->constrained()->onDelete('cascade')
    # related_name='tasks' permite acceder a las tareas de un usuario con user.tasks (equivalente a hasMany en Laravel)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    # auto_now_add=True = se asigna solo al crear (como created_at en Eloquent)
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now=True = se actualiza cada vez que se guarda (como updated_at en Eloquent)
    updated_at = models.DateTimeField(auto_now=True)

    # Equivalente a __toString() en PHP
    # Django lo usa para mostrar el objeto en el admin y en el shell
    def __str__(self):
        return self.title
