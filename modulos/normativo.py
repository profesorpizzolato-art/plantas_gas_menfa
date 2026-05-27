# modulos/normativo.py
import streamlit as st

def render_normativo():
    st.header("⚖️ Entrenamiento Normativo y Cumplimiento de Seguridad")
    st.subheader("Matriz de Inspecciones Obligatorias según NAG-125")
    
    st.markdown("""
    De acuerdo con la reglamentación aplicable a plantas de tratamiento y acondicionamiento de gas, 
    los elementos críticos de protección e interlocks deben cumplir con frecuencias estrictas de control.
    """)
    
    # Tabla de cumplimiento normativo interactiva
    data_norma = {
        "Elemento de Protección": ["Válvulas de Bloqueo (ESD)", "Tanque Espumígeno C/Incendio", "Válvulas de Seguridad (PSV)", "Detectores de Gas/Fuego"],
        "Frecuencia Obligatoria": ["Mensual (Accionamiento)", "Diario (Nivel) / Anual (Ensayo)", "Anual (Calibración)", "Semestral (Contraste)"],
        "Estado en Planta": ["Cumplido ✅", "Cumplido ✅", "Pendiente ⚠️", "Cumplido ✅"]
    }
    st.table(data_norma)
    
    st.warning("⚠️ **Alerta de Auditoría:** La calibración quinquenal de espesores y anual de PSVs en líneas de alta presión está próxima a vencer.")
