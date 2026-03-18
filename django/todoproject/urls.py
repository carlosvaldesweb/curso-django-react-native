"""
URL configuration for todoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # include es equivalente al require de rutas en Laravel
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    # Monta todas las URLs de tasks bajo el prefijo /api/v1/
    # Equivalente a Route::prefix('api/v1')->group(base_path('routes/tasks.php')) en Laravel
    path('api/v1/', include('tasks.urls')),
    # --- Autenticación JWT (simplejwt) ---
    # Flujo completo:
    #   1. POST /api/v1/auth/token/          → manda username+password, recibe access+refresh
    #   2. GET  /api/v1/tasks/               → usa access en header: Authorization: Bearer <access>
    #   3. access expira (5 min por defecto)...
    #   4. POST /api/v1/auth/token/refresh/  → manda refresh, recibe nuevo access
    #   5. Repite desde el paso 2
    #   6. Cuando refresh expira (1 día) → el usuario debe hacer login de nuevo
    #
    # access  → para hacer peticiones. Dura poco por seguridad (si lo roban, solo sirve 5 min)
    # refresh → solo para renovar el access. NO se usa para peticiones a la API
    #
    # Cómo probar con curl:
    #   Login (obtener tokens):
    #     curl -X POST http://localhost:8000/api/v1/auth/token/ \
    #       -H "Content-Type: application/json" \
    #       -d '{"username": "carlosvaldes", "password": "password"}'
    #
    #   Usar el access token en una petición:
    #     curl http://localhost:8000/api/v1/tasks/ \
    #       -H "Authorization: Bearer <access_token>"
    #
    #   Renovar el access token cuando expira:
    #     curl -X POST http://localhost:8000/api/v1/auth/token/refresh/ \
    #       -H "Content-Type: application/json" \
    #       -d '{"refresh": "<refresh_token>"}'
    path('api/v1/auth/token/', TokenObtainPairView.as_view()),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view()),
]
