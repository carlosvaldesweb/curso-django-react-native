from rest_framework import serializers
from django.contrib.auth import get_user_model

# get_user_model() siempre devuelve el modelo configurado en AUTH_USER_MODEL.
# Nunca importes User directamente con "from django.contrib.auth.models import User"
# cuando tienes un modelo personalizado — usa siempre esta función.
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    # write_only=True — este campo solo entra en el request, nunca sale en la respuesta.
    # Equivalente a poner 'password' en $hidden en el modelo User de Laravel.
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # fields define qué campos PARTICIPAN en el serializer (entrada y/o salida).
        # Es como $fillable en Laravel — la lista completa de campos que el serializer conoce.
        # La dirección de cada campo se controla por separado:
        #   - Sin opción → entra Y sale (email: llega en el request y se devuelve en la respuesta)
        #   - write_only=True → solo entra, nunca sale (password)
        #   - read_only=True → solo sale, nunca entra (útil para id, created_at, tokens)
        fields = ['email', 'password']

    # create() se llama cuando el serializer valida y guarda los datos (equivalente a store() en Laravel).
    # Usamos create_user() del UserManager para que la contraseña se hashee correctamente.
    # NUNCA uses User.objects.create() directamente — guardaría la contraseña en texto plano.
    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
