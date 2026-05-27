import streamlit as st

def render_evaluacion():
    st.header("📝 Módulo de Evaluación Operativa")
    
    with st.expander("Comprobar conocimientos técnicos (Manual de Operaciones)"):
        st.write("**Pregunta:** Si ocurre un arrastre severo de líquido desde el separador de entrada hacia la torre contactora de glicol (TEG), ¿cuál es la consecuencia operativa inmediata?")
        
        respuesta = st.radio("Seleccioná la opción correcta:", [
            "Aumenta drásticamente la eficiencia de deshidratación del gas.",
            "Se produce contaminación y espumado del glicol, reduciendo la capacidad de absorción y generando pérdidas por cabeza.",
            "El glicol se congela instantáneamente en la base de la torre."
        ], index=None)
        
        if respuesta:
            if "contaminación y espumado" in respuesta:
                st.success("¡Correcto! El arrastre de hidrocarburos líquidos o agua libre contamina el circuito de glicol provocando espumado (foaming).")
            else:
                st.error("Incorrecto. El líquido de entrada afecta negativamente las propiedades químicas del solvente.")
