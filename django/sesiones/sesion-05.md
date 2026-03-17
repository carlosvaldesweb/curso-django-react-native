# Sesion 5: Configurar PostgreSQL

**Fecha:** 2026-03-17

## Objetivos

- [x] Verificar PostgreSQL instalado (via DBngin)
- [x] Crear la base de datos `tododb`
- [x] Instalar el driver `psycopg` (v3) para Python
- [x] Configurar la conexion en `settings.py`
- [x] Ejecutar migraciones sobre PostgreSQL

## Resumen

1. Se verifico que PostgreSQL estaba corriendo via **DBngin** en el puerto `54321` (version 17)
2. Se creo la base de datos `tododb` manualmente desde **TablePlus**
3. Se instalo `psycopg[binary]` (version 3), el driver moderno de PostgreSQL para Python recomendado por Django 6.0
4. Se reemplazo la configuracion de SQLite por PostgreSQL en `settings.py`
5. Se ejecuto `python manage.py migrate` — Django creo todas las tablas del sistema en `tododb`
6. Se verifico la conexion exitosa viendo las tablas en TablePlus

## Comparaciones con Laravel

### Configuracion de base de datos

| Django (`settings.py`) | Laravel (`.env`) |
|---|---|
| `ENGINE` | `DB_CONNECTION=pgsql` |
| `NAME` | `DB_DATABASE` |
| `USER` | `DB_USERNAME` |
| `PASSWORD` | `DB_PASSWORD` |
| `HOST` | `DB_HOST` |
| `PORT` | `DB_PORT` |

En Laravel la configuracion va en `.env` y Django la tiene directamente en `settings.py`. En una sesion futura la moveremos a variables de entorno con `django-environ` o `python-decouple`.

### Driver de base de datos

| Python/Django | PHP/Laravel |
|---|---|
| `psycopg` (driver Python para PostgreSQL) | Extension `pdo_pgsql` de PHP |
| `pip install "psycopg[binary]"` | Viene incluida con PHP |

### SQLite vs PostgreSQL

SQLite (el default de Django) es equivalente al servidor embebido de PHP — sirve para demos rapidas pero no para produccion. PostgreSQL es la base de datos recomendada para proyectos Django en produccion.

## Comandos clave

```bash
# Instalar el driver de PostgreSQL para Python
pip install "psycopg[binary]"

# Actualizar el registro de dependencias (equivalente a composer.json)
pip freeze > requirements.txt

# Correr migraciones sobre la nueva base de datos
python manage.py migrate
```

## Notas adicionales

- DBngin instala PostgreSQL pero no agrega `psql` al PATH. Se puede usar directamente con `/Applications/DBngin.app/Contents/Library/bin/psql` si se necesita la CLI
- Usamos `HOST: '127.0.0.1'` en lugar de `'localhost'` para forzar conexion TCP en lugar de socket Unix — esto es importante cuando el servidor corre en un puerto no estandar como DBngin
- El puerto `54321` es el default de DBngin para PostgreSQL (el estandar es `5432`)
- `psycopg[binary]` (v3) es el reemplazo moderno de `psycopg2`, recomendado por Django 6.0
