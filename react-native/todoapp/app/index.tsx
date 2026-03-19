// Equivalente a importar componentes en Vue: import { ref } from 'vue'
// View y Text son los componentes base de React Native (no hay HTML aquí)
import { Text, View } from "react-native";

// Componente funcional — equivalente a un <script setup> en un .vue
// El nombre del archivo (index.tsx) define la ruta: / (raíz)
export default function Index() {
  // JSX: HTML dentro de JavaScript — en Vue esto sería el <template>
  return (
    // View = <div> en HTML. Sin View no puedes agrupar elementos.
    // style={{}} inline — equivalente a :style="{}" en Vue
    // flex: 1 hace que ocupe toda la pantalla (como height: 100% en CSS)
    <View
      style={{
        flex: 1,
        justifyContent: "center", // equivalente a justify-content: center en CSS
        alignItems: "center",     // equivalente a align-items: center en CSS
      }}
    >
      {/* Text = <p> o <span> en HTML. En React Native TODO el texto debe estar en <Text> */}
      <Text>Hola desde mi To-Do app.</Text>
      <Text>Sesión 1 completada</Text>
    </View>
  );
}
