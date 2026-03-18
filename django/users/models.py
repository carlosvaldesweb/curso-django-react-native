# Equivalente a app/Models/User.php en Laravel, pero con control total sobre
# cómo se crean los usuarios (sin username, solo email).
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# UserManager centraliza la lógica de creación de usuarios.
# En Laravel esto está disperso entre User::create(), Hash::make() y UserFactory.
# Aquí todo está en un solo lugar.
class UserManager(BaseUserManager):

    # Equivalente a User::create() en Laravel, pero con hasheo de contraseña incluido.
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        # normalize_email convierte el email a minúsculas para evitar duplicados.
        # carlos@Gmail.COM → carlos@gmail.com
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        # set_password hashea la contraseña con bcrypt.
        # Equivalente a Hash::make() en Laravel.
        # NUNCA hagas user.password = "123" directamente — se guardaría en texto plano.
        user.set_password(password)
        # using=self._db permite soporte multi-base de datos (buena práctica).
        user.save(using=self._db)
        return user

    # Equivalente a crear un usuario con rol de administrador.
    # is_staff = puede entrar al Django Admin.
    # is_superuser = tiene todos los permisos sin restricción.
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


# AbstractUser trae campos listos: is_active, is_staff, date_joined, etc.
# Equivalente a extender el modelo User base de Laravel.
class User(AbstractUser):
    # Eliminamos username — Django lo trae por defecto pero las apps modernas no lo usan.
    username = None
    # Redefinimos email para que sea único (por defecto Django no lo garantiza).
    # Equivalente a $table->string('email')->unique() en una migración de Laravel.
    email = models.EmailField(unique=True)

    # Le dice a Django que el campo de autenticación es email, no username.
    # Equivalente a cambiar 'username' en config/auth.php de Laravel.
    USERNAME_FIELD = 'email'
    # Sin campos extra obligatorios al crear superusuario por consola.
    REQUIRED_FIELDS = []

    # Conecta el manager personalizado al modelo.
    # Permite usar User.objects.create_user(...) — en Laravel es User::create().
    objects = UserManager()
