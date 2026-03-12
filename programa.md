# Programa General del Curso

## Objetivo

Construir una aplicacion **To-Do List** completa con:
- **Backend**: Django + Django REST Framework + PostgreSQL
- **Frontend mobile**: React Native con Expo
- **Autenticacion**: Login con correo y contrasena (JWT)
- **CRUD completo**: Crear, editar, eliminar y listar tareas
- **Versionado de API**: Estructura profesional con versionado (v1, v2)

---

## Fase 1 - Fundamentos Backend (Django)

> Comparacion principal: **Django vs Laravel**

| Sesion | Tema | Equivalente Laravel |
|---|---|---|
| 1 | Instalar Python, pip, virtualenv | Instalar PHP, Composer |
| 2 | Crear proyecto Django, explorar estructura | `php artisan`, estructura Laravel |
| 3 | Modelos y migraciones | Eloquent, `php artisan migrate` |
| 4 | Django Admin | Laravel Nova / Filament |
| 5 | Configurar PostgreSQL | Configurar MySQL en `.env` |
| 6 | Django REST Framework - Serializers | API Resources / Transformers |
| 7 | Vistas y URLs para API | Routes y Controllers |
| 8 | CRUD de tareas via API | CRUD en Controller |
| 9 | Modelo User y autenticacion | Auth de Laravel |
| 10 | JWT con simplejwt | Sanctum / Passport |
| 11 | Permisos y proteccion de endpoints | Middleware, Gates, Policies |
| 12 | Versionado de APIs (v1, v2) | No es comun en web monolitico |
| 13 | Testing | PHPUnit |

**Resultado**: API REST completa y funcional para la To-Do List.

---

## Fase 2 - Fundamentos Frontend (React Native)

> Comparacion principal: **React Native vs Vue/Nuxt**

| Sesion | Tema | Equivalente Vue/Nuxt |
|---|---|---|
| 1 | Instalar Node, Expo CLI, crear proyecto | `npx nuxi init`, estructura Nuxt |
| 2 | JSX y componentes | Templates Vue y SFC (`.vue`) |
| 3 | Props y State (useState) | Props, `ref()`, `reactive()` |
| 4 | useEffect y ciclo de vida | `onMounted`, `watch`, `watchEffect` |
| 5 | Estilos en React Native | CSS / Tailwind en Vue |
| 6 | Navegacion (React Navigation) | Vue Router / NuxtLink |
| 7 | Formularios y validacion | v-model, VeeValidate |
| 8 | Llamadas a API (fetch/axios) | `useFetch`, `$fetch` de Nuxt |
| 9 | Context API / estado global | Pinia / Vuex |
| 10 | Pantalla de Login y registro | Paginas auth en Nuxt |
| 11 | CRUD de tareas conectado al backend | Componentes con fetch en Nuxt |
| 12 | AsyncStorage para tokens | localStorage / cookies |

**Resultado**: App mobile funcional que consume la API de Django.

---

## Fase 3 - Integracion

| Sesion | Tema |
|---|---|
| 1 | Conectar React Native con Django API (CORS, configuracion) |
| 2 | Flujo completo de autenticacion (registro, login, tokens) |
| 3 | CRUD de tareas end-to-end |
| 4 | Versionado de API en la practica (consumir v1 desde la app) |
| 5 | Manejo de errores y estados de carga |

**Resultado**: App completa funcionando de punta a punta.

---

## Fase 4 - Pulido y extras

| Sesion | Tema |
|---|---|
| 1 | Mejoras de UX (pull to refresh, feedback visual) |
| 2 | Validaciones robustas (frontend y backend) |
| 3 | Preparar para produccion (variables de entorno, configuracion) |

**Resultado**: App lista para demostrar o subir a tiendas.

---

## Notas

- Las sesiones son **estimadas**. Algunas pueden tomar mas o menos tiempo dependiendo del ritmo.
- Las fases 1 y 2 pueden avanzar en **paralelo** si se desea (una sesion de Django, una de React Native).
- Cada sesion genera un **resumen** y un **commit con tag** en Git.
- El programa detallado de cada tecnologia esta en:
  - [django/programa-django.md](django/programa-django.md)
  - [react-native/programa-react-native.md](react-native/programa-react-native.md)
