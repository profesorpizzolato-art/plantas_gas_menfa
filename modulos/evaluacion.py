# modulos/evaluacion.py
import streamlit as st

def render_evaluacion():
    st.header("📝 Sistema de Evaluación de Competencias Técnicas")
    st.caption("Examen teórico-práctico auditable para habilitación de puestos operativos.")
    
    st.info("Responda las siguientes preguntas del módulo de planta. Al finalizar, presione 'Calificar Examen'.")
    
    # Pregunta 1
    p1 = st.radio("1. ¿Cuál es el límite máximo de humedad permitido para el gas de entrega en gasoductos?",
                  ["100 mg/m³", "64 mg/m³", "20 mg/m³"], index=None)
    
    # Pregunta 2
    p2 = st.radio("2. ¿Qué acción automática genera el accionamiento del interruptor de nivel Alto-Alto en el separador?",
                  ["Abrir el bypass de la planta", "Activar el Cierre de Emergencia (CDE) cerrando válvulas de bloqueo", "Encender la bomba de amina"], index=None)
    
    if st.button("📊 Calificar Examen"):
        nota = 0
        if p1 == "64 mg/m³": nota += 50
        if p2 == "Activar el Cierre de Emergencia (CDE) cerrando válvulas de bloqueo": nota += 50
        
        st.subheader(f"Resultado Final: {nota} / 100")
        if nota >= 70:
            st.success("🎉 OPERADOR APROBADO. Cumple con los requisitos teóricos mínimos.")
        else:
            st.error("❌ OPERADOR DESAPROBADO. Requiere revisión del Manual Digital.")
