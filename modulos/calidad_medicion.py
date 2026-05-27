# modulos/calidad_medicion.py
import streamlit as st
import config as cfg

def render_calidad_medicion():
    st.header("🔬 Control de Calidad y Transferencia de Custodia")
    st.subheader("Monitoreo de Componentes Fuera de Especificación Comercial")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Humedad Actual", f"{st.session_state.humedad_salida:.1f} mg/m³", delta="OK" if st.session_state.humedad_salida <= cfg.LIMITE_HUMEDAD else "FUERA DE NORMA", delta_color="inverse")
    col2.metric("Contenido H2S", "2.1 ppm", delta="OK")
    col3.metric("Contenido CO2", "1.4 %", delta="OK")
    
    st.info("💡 **Punto de Rocío (Dew Point):** El control estricto del punto de rocío de hidrocarburos e hidratos evita la condensación retrógrada en las cañerías del gasoducto principal.")
