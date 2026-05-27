# modulos/seguridad.py
import streamlit as st
import config as cfg

def render_seguridad():
    st.header("🛡️ Matriz de Enclavamientos de Seguridad (ESD / CDE)")
    
    cde = False
    motivos = []
    
    if st.session_state.nivel_liquido >= cfg.NIVEL_MAX_SEPARADOR:
        cde = True
        motivos.append("Inundación / Alto nivel crítico en Separador de entrada.")
    if st.session_state.p_entrada >= cfg.PRESION_MAX_PLANTA:
        cde = True
        motivos.append("Sobrepresión crítica en Colector principal.")
    if st.session_state.temp_reboiler >= cfg.TEMP_MAX_REBOILER:
        cde = True
        motivos.append("Alta temperatura crítica en Reboiler de Glicol.")
        
    if cde:
        st.error("🚨 CIERRE DE EMERGENCIA AUTOMÁTICO ACTIVADO (CDE)")
        for m in motivos:
            st.write(f"❌ **Causa del Disparo:** {m}")
        st.warning("⚠️ **Acción Mecánica:** Bloqueo automático de válvulas de entrada y despresurización segura por antorcha (Vent).")
    else:
        st.success("🟢 SISTEMA DE ENCLAVAMIENTO EN LÍNEA - SIN ALARMAS ACTIVAS")
