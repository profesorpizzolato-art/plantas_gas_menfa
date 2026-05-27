# modulos/separacion.py
import streamlit as st

def render_separacion():
    st.header("🛢️ Sistema de Separación de Entrada (Slug Catchers)")
    col1, col2 = st.columns([1, 2])
    with col1:
        p_entrada = st.slider("Presión Colector de Entrada (kPa)", 1000, 7500, int(st.session_state.p_entrada), step=100)
        t_entrada = st.slider("Temperatura de Entrada (°C)", -10, 50, int(st.session_state.t_entrada))
        nivel_liquido = st.slider("Nivel de Líquidos en Tanque (%)", 0, 100, int(st.session_state.nivel_liquido))
    with col2:
        st.info(f"Presión actual: **{p_entrada} kPa** | Temperatura: **{t_entrada} °C**")
        st.progress(nivel_liquido / 100.0)
        st.caption(f"Capacidad del acumulador de líquidos al {nivel_liquido}%")
    return p_entrada, t_entrada, nivel_liquido
