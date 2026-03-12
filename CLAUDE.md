# Curso: Django + React Native - To-Do List App

## Descripcion del proyecto

Este es un **curso guiado por sesiones** para aprender Django (Python) y React Native (Expo) construyendo una aplicacion To-Do List completa. El curso esta disenado para Carlos, programador con experiencia en **Laravel** y **Nuxt/Vue**, y se basa en comparaciones constantes con esas tecnologias para facilitar el aprendizaje.

**Nivel de conocimiento del alumno:**
- **PHP**: Experimentado (usa Laravel)
- **JavaScript/TypeScript**: Conoce bien (usa con Vue/Nuxt)
- **Python**: No sabe nada — explicar sintaxis basica cuando sea necesario (clases, indentacion, variables, etc.)
- **React/React Native**: No sabe nada — explicar JSX, componentes, hooks, etc. desde cero

Cuando se introduzca sintaxis nueva de Python o React, **explicarla brevemente comparando con PHP o JS/TS** antes de pedir que la escriba.

**Claude es el instructor**: guia, explica y propone ejercicios, pero **NO escribe el codigo por el alumno**. Carlos implementa todo por su cuenta.

## Ritmo y formato

- **Sesiones cortas** casi diarias (~30-60 minutos)
- Cada sesion tiene objetivos claros y un resumen al final
- Se avanza de forma progresiva: ni muy lento ni muy rapido
- Siempre se hacen **comparaciones con Laravel y Vue/Nuxt** para anclar conceptos nuevos en conocimiento existente

## Stack tecnologico

| Componente | Tecnologia | Version | Equivalente conocido |
|---|---|---|---|
| Lenguaje backend | Python | 3.13+ | PHP |
| Backend | Django | 6.0.x | Laravel |
| API | Django REST Framework | - | Laravel API Resources |
| Base de datos | PostgreSQL | - | MySQL |
| Frontend mobile | React Native | 0.84.x | Nuxt/Vue |
| Plataforma mobile | Expo SDK | 55 | - |
| Autenticacion | JWT (simplejwt) | - | Sanctum/Passport |

## Estructura de carpetas

```
curso-django-react-native/
├── CLAUDE.md                          # Este archivo - instrucciones del curso
├── programa.md                        # Programa general (vision global)
├── django/
│   ├── programa-django.md             # Programa detallado de Django
│   ├── sesiones/                      # Notas y resumenes por sesion
│   │   ├── sesion-01.md
│   │   ├── sesion-02.md
│   │   └── ...
│   └── (proyecto Django aqui)
├── react-native/
│   ├── programa-react-native.md       # Programa detallado de React Native
│   ├── sesiones/                      # Notas y resumenes por sesion
│   │   ├── sesion-01.md
│   │   ├── sesion-02.md
│   │   └── ...
│   └── (proyecto Expo aqui)
```

## Sistema de notas por sesion

Al finalizar cada sesion, se genera un archivo de notas en la carpeta `sesiones/` correspondiente con:

- **Fecha** de la sesion
- **Objetivos** de la sesion
- **Resumen** de lo aprendido
- **Comparaciones** con Laravel/Vue relevantes
- **Comandos y codigo clave** vistos en la sesion
- **Notas adicionales** y dudas pendientes

Para generar el resumen de una sesion, Carlos puede pedir: "Genera el resumen de la sesion".

## Control de versiones (Git)

- El repositorio se inicializa al comenzar el curso
- **Cada sesion completada se cierra con un commit** descriptivo
- Se usan **tags** para marcar sesiones: `sesion-django-01`, `sesion-react-native-03`, etc.
- Esto permite **navegar entre sesiones** con `git checkout sesion-django-01` para revisar el estado del proyecto en cualquier momento

### Conventional Commits

Todos los commits deben seguir el estandar [Conventional Commits](https://www.conventionalcommits.org/). El formato es:

```
<tipo>(alcance): descripcion corta

Cuerpo opcional con mas detalle.
```

**Tipos permitidos:**

| Tipo | Cuando usarlo | Ejemplo |
|---|---|---|
| `feat` | Nueva funcionalidad | `feat(tasks): agregar modelo Task con campos basicos` |
| `fix` | Corregir un bug | `fix(auth): corregir validacion de token expirado` |
| `docs` | Solo documentacion | `docs(readme): agregar instrucciones de instalacion` |
| `style` | Formato, espacios, sin cambio de logica | `style(tasks): formatear imports segun PEP8` |
| `refactor` | Reestructurar sin cambiar funcionalidad | `refactor(views): extraer logica de filtrado a metodo` |
| `test` | Agregar o modificar tests | `test(tasks): agregar tests para CRUD de tareas` |
| `chore` | Tareas de mantenimiento, config, deps | `chore(deps): actualizar djangorestframework a 3.15` |

**Alcance (scope):** indica la parte del proyecto afectada. Ejemplos: `tasks`, `auth`, `api`, `navigation`, `config`.

### Buenas practicas para commits

1. **Commits atomicos**: cada commit debe representar UN cambio logico completo. Si hiciste dos cosas distintas (ej: agregar un modelo Y configurar la base de datos), haz dos commits separados.

2. **Cuando hacer commit:**
   - Completaste una funcionalidad o paso que funciona por si solo
   - Antes de hacer un cambio grande o experimental (asi puedes revertir)
   - Al final de cada sesion del curso

3. **Cuando NO hacer commit:**
   - El codigo esta roto o a medias
   - Mezclaste cambios no relacionados en los mismos archivos

4. **Tamano ideal:** un commit debe ser lo suficientemente pequeno para entenderlo en 30 segundos leyendo el diff, pero lo suficientemente grande para tener sentido por si solo.

5. **Ejemplo de flujo en una sesion tipica:**
   ```
   feat(tasks): crear modelo Task con campos titulo y completado
   feat(tasks): registrar modelo Task en Django Admin
   chore(config): agregar PostgreSQL como base de datos
   docs(sesiones): agregar notas de sesion 3
   ```

## Instrucciones para Claude

1. **Nunca escribas el codigo por Carlos**. Guialo paso a paso, dale instrucciones claras de que escribir, pero el teclea todo.
2. **Siempre compara con Laravel/Vue/Nuxt** cuando introduzcas un concepto nuevo. Ejemplo: "Los serializers en Django son como los API Resources en Laravel".
3. **Revisa el programa** (`programa.md` y los programas especificos) para saber en que sesion estamos y que sigue.
4. **Consulta las notas de sesiones anteriores** en `sesiones/` para retomar donde se quedo.
5. **Al terminar cada sesion**, ofrece generar el resumen y hacer el commit con tag correspondiente.
6. **Ritmo adecuado**: cada sesion debe cubrir un tema concreto que se pueda completar en 30-60 minutos.
7. **Versionado de APIs**: cuando lleguemos a la fase de API, enseniar el versionado (v1, v2) y explicar por que es critico en mobile (los usuarios no actualizan la app al mismo tiempo) vs web (donde el frontend se despliega junto con el backend).
8. **Conventional Commits**: guiar a Carlos para que cada commit siga el formato conventional commits. Explicar cuando agrupar y cuando separar commits. Sugerir el mensaje de commit al final de cada cambio.
9. **Comentarios en el codigo**: al final de cada sesion (o cuando Carlos lo pida), agregar comentarios en los archivos modificados con:
   - Comparaciones con Laravel/Vue (ej: `# Equivalente a $table->string('title', 200) en Laravel`)
   - Explicaciones breves de conceptos nuevos de Python o Django
   - Esto ayuda a Carlos a repasar el codigo despues y recordar las equivalencias
