# modulos/normativo.py
import streamlit as st

def render_normativo():
    st.header("⚖️ Pilar 3: Entrenamiento Normativo (Norma NAG-125)")
    st.write("Cronograma mandatorio de inspección y calibración periódica exigido por Gas del Estado.")
    
    cronograma = {
        "Elemento de Seguridad": ["Válvulas de Cierre de Emergencia (ESD)", "Detectores de Mezclas Explosivas", "Válvulas de Alivio de Presión (PSV)"],
        "Frecuencia de Ensayo Legal": ["Mensual (Accionamiento completo)", "Semestral (Contraste y Calibración)", "Anual (Desmontaje y Banco)"],
        "Estado de Cumplimiento": ["CUMPLIDO ✅", "CUMPLIDO ✅", "VENCIDO ⚠️ Requiere Calibración"]
    }
    st.table(cronograma)
    st.warning("🚨 **Alerta de Auditoría:** La PSV del colector registra 14 meses desde su último ensayo. Regularizar de inmediato.")
