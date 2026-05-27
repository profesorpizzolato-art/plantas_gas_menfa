# modulos/evaluacion.py
import streamlit as st

def render_evaluacion():
    st.header("📝 Pilar 2: Sistema de Evaluación de Competencia")
    st.write("Responda el cuestionario obligatorio de operaciones de planta (Mínimo aprobación: 70%).")
    st.markdown("---")
    
    p1 = st.radio("1. ¿Cuál es la concentración de humedad máxima permitida para el gas de entrega?", ["100 mg/m³", "64 mg/m³", "40 mg/m³"], index=None)
    p2 = st.radio("2. ¿Qué fenómeno ocurre si ingresan hidrocarburos líquidos a la torre de TEG?", ["Aumenta la absorción.", "Se genera espumado (foaming) del solvente con arrastre por cabeza.", "El glicol se congela."], index=None)
    
    if st.button("📊 Calificar Evaluación"):
        nota = 0
        if p1 == "64 mg/m³": nota += 50
        if p2 == "Se genera espumado (foaming) del solvente con arrastre por cabeza.": nota += 50
        st.subheader(f"Puntaje Obtenido: {nota} / 100")
        if nota >= 70: st.success("🎉 OPERADOR APROBADO.")
        else: st.error("❌ RECHAZADO. Repase el manual técnico.")
