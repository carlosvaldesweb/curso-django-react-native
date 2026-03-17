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

urlpatterns = [
    path('admin/', admin.site.urls),
    # Monta todas las URLs de tasks bajo el prefijo /api/
    # Equivalente a Route::prefix('api')->group(base_path('routes/tasks.php')) en Laravel
    path('api/', include('tasks.urls'))
]
