# modulos/transporte.py
import streamlit as st
import numpy as np
import pandas as pd

def render_transporte():
    st.header("🚀 Estación Compresora y Control de Gasoductos")
    col1, col2 = st.columns(2)
    with col1:
        p_succion = st.slider("Presión de Succión (kPa)", 2000, 4500, 3200)
        p_descarga = st.slider("Presión de Descarga (kPa)", 4500, 8000, int(st.session_state.p_descarga_gasoducto))
    with col2:
        rc = (p_descarga + 101.3) / (p_succion + 101.3)
        st.metric("Relación de Compresión (Rc)", f"{rc:.2f}")
        
        distancia = np.linspace(0, 100, 50)
        presion_linea = p_descarga - (distancia * 12)
        df = pd.DataFrame({"Presión en Línea (kPa)": presion_linea}, index=distancia)
        st.line_chart(df)
    return p_descarga
