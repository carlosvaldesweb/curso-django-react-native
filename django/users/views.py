# Equivalente a AuthController en Laravel — maneja registro y autenticación de usuarios.
from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer

# Siempre usa get_user_model() en vez de importar User directamente.
# Garantiza que se use el modelo configurado en AUTH_USER_MODEL.
User = get_user_model()


# CreateAPIView maneja automáticamente POST — equivalente a un controlador
# con solo el método store() en Laravel.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # AllowAny — endpoint público, no requiere token.
    # Sin esto nadie podría registrarse porque necesitaría un token para... obtener un token.
    # Equivalente a una ruta sin middleware 'auth' en Laravel.
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    # Sobreescribimos create() para agregar los tokens JWT en la respuesta.
    # Si no lo hiciéramos, CreateAPIView devolvería solo los datos del serializer (email).
    # Equivalente a sobreescribir store() en un ResourceController de Laravel.
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # is_valid(raise_exception=True) valida los datos y lanza un 400 automáticamente si fallan.
        # Equivalente a $request->validate([...]) en Laravel.
        serializer.is_valid(raise_exception=True)
        # save() llama a create() del serializer, que usa create_user() para hashear la contraseña.
        user = serializer.save()

        # Genera el par de tokens JWT para el usuario recién creado.
        # Así el usuario queda logueado automáticamente al registrarse — sin segundo request.
        # Equivalente a $user->createToken() en Laravel Sanctum.
        refresh = RefreshToken.for_user(user)

        return Response({
            'email': user.email,
            # access → token de corta duración para hacer peticiones a la API
            'access': str(refresh.access_token),
            # refresh → token de larga duración solo para renovar el access cuando expira
            'refresh': str(refresh),
        })
