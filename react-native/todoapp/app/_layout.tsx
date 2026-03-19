// expo-router maneja la navegación basada en archivos — igual que Nuxt con su carpeta pages/
import { Stack } from "expo-router";

// Layout raíz — equivalente a app.vue o layouts/default.vue en Nuxt
// Envuelve TODAS las pantallas de la app
export default function RootLayout() {
  // Stack = navegación en pila (pantallas se apilan una sobre otra)
  // Equivalente a <NuxtPage /> en Nuxt, pero con animación de "push" estilo mobile
  return <Stack />;
}
