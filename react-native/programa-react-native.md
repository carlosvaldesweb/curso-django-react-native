# Programa Detallado: React Native (Expo)

## Progreso

| Sesion | Estado |
|---|---|
| 1-12 | Pendiente |

---

## Sesion 1: Instalacion y primer proyecto con Expo

**Objetivos:**
- Verificar Node.js instalado (o instalarlo)
- Instalar Expo CLI
- Crear un proyecto nuevo con `npx create-expo-app`
- Ejecutar la app en el simulador/dispositivo fisico
- Explorar la estructura del proyecto

**Comparacion con Vue/Nuxt:**
| React Native (Expo) | Vue/Nuxt |
|---|---|
| `npx create-expo-app` | `npx nuxi init` |
| `npx expo start` | `npm run dev` |
| `app/` o `App.js` | `pages/`, `app.vue` |
| `package.json` | `package.json` |
| Metro bundler | Vite |
| Expo Go (app para probar) | Navegador web |

---

## Sesion 2: JSX y componentes

**Objetivos:**
- Entender JSX (HTML dentro de JavaScript)
- Crear componentes funcionales
- Diferencia entre `View`, `Text`, `TouchableOpacity` (no hay HTML en mobile)
- Importar y usar componentes

**Comparacion con Vue/Nuxt:**
| React Native | Vue |
|---|---|
| JSX (HTML en JS) | Template (HTML separado en `<template>`) |
| `function MiComponente() {}` | `<script setup>` en SFC |
| `<View>` | `<div>` |
| `<Text>` | `<p>`, `<span>` |
| `<TouchableOpacity>` | `<button>` |
| `<Image>` | `<img>` |
| Todo es JS: logica y markup juntos | Separacion: template, script, style |

---

## Sesion 3: Props y State (useState)

**Objetivos:**
- Pasar datos a componentes con Props
- Manejar estado local con `useState`
- Entender la re-renderizacion cuando cambia el state
- Ejercicio: contador simple y lista estatica

**Comparacion con Vue/Nuxt:**
| React | Vue 3 (Composition API) |
|---|---|
| `useState(valorInicial)` | `ref(valorInicial)` |
| `const [count, setCount] = useState(0)` | `const count = ref(0)` |
| `setCount(count + 1)` para actualizar | `count.value++` para actualizar |
| Props son parametros de la funcion | `defineProps()` |
| Inmutabilidad: siempre `setX(nuevoValor)` | Mutabilidad: `count.value = 5` |
| Re-render completo del componente | Reactividad granular (solo lo que cambio) |

---

## Sesion 4: useEffect y ciclo de vida

**Objetivos:**
- Entender `useEffect` y cuando se ejecuta
- Simular `onMounted` (ejecutar algo al montar el componente)
- Dependencias de `useEffect` (array de dependencias)
- Cleanup de efectos

**Comparacion con Vue/Nuxt:**
| React | Vue 3 |
|---|---|
| `useEffect(() => {}, [])` | `onMounted(() => {})` |
| `useEffect(() => {}, [dep])` | `watch(dep, () => {})` |
| `useEffect(() => {})` (sin deps) | `watchEffect(() => {})` |
| Return en useEffect = cleanup | `onUnmounted(() => {})` |
| Un solo hook para todo | Hooks especificos por etapa |

---

## Sesion 5: Estilos en React Native

**Objetivos:**
- `StyleSheet.create()` para definir estilos
- Diferencias con CSS web (no hay cascada, no hay clases)
- Flexbox como sistema de layout principal
- Estilos condicionales y dinamicos

**Comparacion con Vue/Nuxt:**
| React Native | Vue/CSS |
|---|---|
| `StyleSheet.create({})` | `<style scoped>` |
| No hay CSS, todo es objetos JS | CSS estandar o Tailwind |
| `backgroundColor` (camelCase) | `background-color` (kebab-case) |
| Flexbox por defecto (`flexDirection: 'column'`) | Necesitas declarar `display: flex` |
| No hay cascada de estilos | CSS tiene cascada y herencia |
| `style={[estiloBase, estiloCondicional]}` | `:class="{ activo: esActivo }"` |

---

## Sesion 6: Navegacion (React Navigation)

**Objetivos:**
- Instalar React Navigation
- Stack Navigator (navegacion tipo "pila" entre pantallas)
- Tab Navigator (barra inferior con pestanas)
- Navegar entre pantallas y pasar parametros

**Comparacion con Vue/Nuxt:**
| React Navigation | Vue Router / Nuxt |
|---|---|
| `createStackNavigator()` | `<NuxtPage>` con rutas |
| `navigation.navigate('Detalle')` | `router.push('/detalle')` |
| `route.params` | `route.params` o `useRoute()` |
| Tab Navigator | No tiene equivalente directo (es patron mobile) |
| Navegacion basada en componentes | Navegacion basada en archivos (Nuxt) |
| Drawer Navigator | Sidebar manual |

---

## Sesion 7: Formularios y validacion

**Objetivos:**
- Inputs con `TextInput`
- Manejar estado del formulario con useState
- Validacion basica de campos
- Enviar datos del formulario

**Comparacion con Vue/Nuxt:**
| React Native | Vue |
|---|---|
| `<TextInput value={x} onChangeText={setX} />` | `<input v-model="x" />` |
| Estado manual con useState por campo | `v-model` two-way binding automatico |
| Validacion manual o con libreria | VeeValidate, Vuelidate |
| No hay `v-model` | `v-model` es azucar sintactico |
| `onSubmitEditing` | `@submit` |

---

## Sesion 8: Llamadas a API (fetch/axios)

**Objetivos:**
- Hacer llamadas HTTP con `fetch` o `axios`
- GET, POST, PUT, DELETE
- Manejar loading y errores
- Mostrar datos de la API en la pantalla

**Comparacion con Vue/Nuxt:**
| React Native | Nuxt/Vue |
|---|---|
| `fetch()` nativo o `axios` | `useFetch()`, `$fetch`, `axios` |
| useState + useEffect para data fetching | `useFetch()` o `useAsyncData()` |
| Manejo manual de loading/error | `useFetch` maneja loading/error automaticamente |
| No hay SSR (es mobile) | SSR/SSG disponible en Nuxt |

---

## Sesion 9: Context API / estado global

**Objetivos:**
- Entender el problema de "prop drilling"
- Crear un Context para estado global
- Provider y Consumer
- Caso de uso: estado de autenticacion global

**Comparacion con Vue/Nuxt:**
| React Context | Pinia (Vue) |
|---|---|
| `createContext()` | `defineStore()` |
| `<Provider value={}>` | `app.use(pinia)` |
| `useContext(MiContexto)` | `useStore()` |
| Basico, puede necesitar useReducer | Mas completo: state, getters, actions |
| Re-render de todo el arbol de consumers | Reactividad granular |

---

## Sesion 10: Pantalla de Login y registro

**Objetivos:**
- Crear pantalla de Login (correo + contrasena)
- Crear pantalla de Registro
- Conectar con la API de autenticacion de Django
- Guardar el token recibido
- Redirigir al usuario autenticado

---

## Sesion 11: CRUD de tareas conectado al backend

**Objetivos:**
- Pantalla de lista de tareas (con datos reales de la API)
- Pantalla para crear nueva tarea
- Editar tarea existente
- Eliminar tarea (con confirmacion)
- Marcar tarea como completada

---

## Sesion 12: AsyncStorage para tokens

**Objetivos:**
- Instalar y usar AsyncStorage
- Persistir el token JWT para mantener la sesion
- Verificar token al abrir la app
- Implementar logout (limpiar token)

**Comparacion con Vue/Nuxt:**
| React Native | Vue/Nuxt (web) |
|---|---|
| `AsyncStorage` | `localStorage` |
| `await AsyncStorage.setItem('token', valor)` | `localStorage.setItem('token', valor)` |
| Asincrono (siempre con await) | Sincrono |
| Persistente entre sesiones | Persistente (localStorage) o por sesion (sessionStorage) |
| No hay cookies en mobile | Cookies disponibles en web |
