# Sesión 1 - React Native: Instalación y primer proyecto con Expo

**Fecha:** 2026-03-18

---

## Objetivos

- Verificar Node.js instalado
- Crear un proyecto con Expo
- Ejecutar la app en el simulador de iOS
- Explorar la estructura del proyecto
- Entender los componentes base: `View` y `Text`

---

## Resumen

Se creó el proyecto Expo dentro de `react-native/todoapp/` usando `npx create-expo-app@latest`. Se ejecutó en el simulador de iOS con `npx expo start` + tecla `i`. Se hizo un reset del proyecto (`npm run reset-project`) para partir de una base limpia, moviendo el template de ejemplo a `app-example/`.

Se exploraron los dos archivos clave del proyecto limpio:
- `app/_layout.tsx` — layout raíz, equivalente a `app.vue` en Nuxt
- `app/index.tsx` — pantalla principal, equivalente a `pages/index.vue` en Nuxt

Se modificó `index.tsx` para mostrar texto personalizado y se comprobó el hot reload funcionando.

---

## Comparaciones con Vue/Nuxt

| React Native (Expo) | Vue/Nuxt |
|---|---|
| `npx create-expo-app` | `npx nuxi init` |
| `npx expo start` | `npm run dev` |
| Metro bundler | Vite |
| `app/index.tsx` → ruta `/` | `pages/index.vue` → ruta `/` |
| `_layout.tsx` | `app.vue` / `layouts/default.vue` |
| `<Stack>` | `<NuxtPage>` |
| `<View>` | `<div>` |
| `<Text>` | `<p>`, `<span>` |
| JSX (HTML dentro de JS) | `<template>` separado en `.vue` |
| `style={{}}` inline | `:style="{}"` en Vue |

---

## Conceptos clave

- **JSX**: HTML escrito dentro de JavaScript. En Vue el HTML va en `<template>`, en React todo está junto en la función del componente.
- **File-based routing**: igual que Nuxt, el nombre del archivo define la ruta. `index.tsx` = ruta `/`.
- **`<View>`**: contenedor obligatorio. No hay `<div>` en React Native.
- **`<Text>`**: todo el texto debe ir dentro de `<Text>`, no se puede poner texto suelto.
- **`npx`**: ejecuta paquetes sin instalarlos globalmente (a diferencia de `npm install`).
- **Stack Navigator**: navegación en pila — las pantallas se apilan y el botón "atrás" las quita.

---

## Comandos clave

```bash
# Crear proyecto Expo
npx create-expo-app@latest todoapp

# Arrancar el servidor de desarrollo
npx expo start

# Abrir en simulador iOS (dentro del menú de Metro)
i

# Limpiar el proyecto de ejemplo
npm run reset-project
```

---

## Notas adicionales

- Los `warn deprecated` al instalar son normales — son dependencias internas de Expo.
- No se puede instalar Expo en una carpeta llamada `react-native` porque conflictúa con el paquete del mismo nombre.
- `app-example/` contiene el template original por si se quiere consultar como referencia.
