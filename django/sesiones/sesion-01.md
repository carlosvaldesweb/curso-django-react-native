# Sesión 1: Instalación de Python y entorno de desarrollo

**Fecha:** 2026-03-11

## Objetivos

- [x] Verificar la versión de Python instalada
- [x] Entender qué es `pip` (el Composer de Python)
- [x] Crear un entorno virtual con `venv`
- [x] Instalar Django dentro del entorno virtual
- [x] Generar `requirements.txt`

## Resumen

Se preparó el entorno de desarrollo para trabajar con Django:

1. **Python 3.14** ya estaba instalado vía Homebrew
2. **pip 25.2** disponible como gestor de paquetes
3. Se creó un **entorno virtual** (`venv`) dentro de `django/` para aislar las dependencias del proyecto
4. Se instaló **Django 6.0.3** dentro del entorno virtual
5. Se generó `requirements.txt` con `pip freeze` para congelar las versiones

## Comparaciones con Laravel

| Concepto | Python/Django | PHP/Laravel |
|---|---|---|
| Lenguaje | `python3` | `php` |
| Gestor de paquetes | `pip` | `composer` |
| Aislamiento de dependencias | `venv` (entorno virtual) | `vendor/` (parcial, PHP es global) |
| Instalar framework | `pip install django` | `composer create-project laravel/laravel` |
| Archivo de dependencias | `requirements.txt` | `composer.json` / `composer.lock` |
| Congelar versiones | `pip freeze > requirements.txt` | Automático con `composer.lock` |

## Comandos clave

```bash
# Verificar versiones
python3 --version
pip3 --version

# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# Verificar que el venv está activo
which python
which pip

# Instalar Django
pip install django

# Verificar versión de Django
python -m django --version

# Congelar dependencias
pip freeze > requirements.txt

# Desactivar entorno virtual
deactivate
```

## Notas adicionales

- **Siempre activar el venv** antes de trabajar: `source venv/bin/activate`. Si no ves `(venv)` en el prompt, el entorno no está activo.
- `pip freeze` es manual a diferencia de `composer.lock` que se genera automáticamente.
- Django 6.0.3 trae dos dependencias: `asgiref` (servidor async) y `sqlparse` (parser SQL).
